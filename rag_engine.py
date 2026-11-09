import os
import numpy as np
from google import genai
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class DomainRAGEngine:

    def __init__(self, data_dir: str = "./data"):
        self.data_dir = data_dir
        self.encoder = SentenceTransformer("BAAI/bge-small-en-v1.5")
        self.documents = []
        self.document_embeddings = None
        self.sources = []

        # Read API key from environment variable
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError(
                "API key not found. Please set GEMINI_API_KEY in your environment or .env file."
            )

        self.client = genai.Client(api_key=api_key)
        self.gemini_model = "gemini-2.5-flash"

    def initialize_knowledge_base(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            sample_path = os.path.join(self.data_dir, "sample_policy.txt")
            if not os.path.exists(sample_path):
                with open(sample_path, "w", encoding="utf-8") as f:
                    f.write(
                        "Company Policy Section 4.2: Employees get 20 days of paid leave"
                        " annually. Remote work requires manager approval 48 hours in"
                        " advance."
                    )

        for filename in os.listdir(self.data_dir):
            if filename.endswith(".txt"):
                file_path = os.path.join(self.data_dir, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read()
                    chunks = [text[i : i + 400] for i in range(0, len(text), 350)]
                    for chunk in chunks:
                        if chunk.strip():
                            self.documents.append(chunk)
                            self.sources.append(filename)

        if self.documents:
            embeddings_array = self.encoder.encode(
                self.documents, convert_to_numpy=True
            )
            norms = np.linalg.norm(embeddings_array, axis=1, keepdims=True)
            self.document_embeddings = embeddings_array / np.maximum(norms, 1e-10)

    def query(self, user_query: str):
        if not self.documents:
            return {"answer": "No documents loaded.", "sources": []}

        query_emb = self.encoder.encode([user_query], convert_to_numpy=True)
        query_norm = np.linalg.norm(query_emb, axis=1, keepdims=True)
        query_emb = query_emb / np.maximum(query_norm, 1e-10)

        similarities = np.dot(self.document_embeddings, query_emb.T).flatten()
        top_k_indices = similarities.argsort()[::-1][:3]

        retrieved_docs = [self.documents[i] for i in top_k_indices]
        retrieved_sources = [self.sources[i] for i in top_k_indices]

        context = "\n\n".join(retrieved_docs)

        prompt = f"""You are a strict domain-specific corporate AI assistant. Answer the user query ONLY using the provided context. If the answer is not in the context, respond with "I cannot find this information in the official knowledge base."

Context:
{context}

Question: 
{user_query}

Answer:"""

        try:
            response = self.client.models.generate_content(
                model=self.gemini_model, contents=prompt
            )
            answer = response.text.strip()
        except Exception as e:
            answer = f"API connection error: {str(e)}"

        return {"answer": answer, "sources": list(set(retrieved_sources))}