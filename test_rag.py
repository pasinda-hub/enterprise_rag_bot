from rag_engine import DomainRAGEngine

# Initialize and load knowledge base
print("Initializing RAG Engine...")
engine = DomainRAGEngine()
engine.initialize_knowledge_base()

# Test query
query_text = "How many days of paid leave do employees get?"
print(f"\nQuerying: '{query_text}'\n")

result = engine.query(query_text)
print("--- RESPONSE ---")
print("Answer:", result["answer"])
print("Sources:", result["sources"])