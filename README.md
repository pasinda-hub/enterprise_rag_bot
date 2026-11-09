# 🏢 Enterprise Policy RAG Assistant

A local-first, privacy-focused Enterprise Policy Chatbot powered by **FastAPI**, **Sentence-Transformers**, and the **Google Gemini API**. 

This system embeds local corporate policy documents using `BAAI/bge-small-en-v1.5`, performs cosine similarity vector searches locally, and uses Google Gemini (`gemini-3.8-flash`) to generate grounded, context-aware answers complete with document source attribution.

---

## 🌟 Key Features

* **Local Semantic Context & Vector Search:** Fast, local embeddings generated via HuggingFace `sentence-transformers` (`BAAI/bge-small-en-v1.5`).
* **Gemini LLM Integration:** Powered by Google's `gemini-3.8-flash` model for enterprise response generation.
* **Futuristic Glassmorphic Web UI:** Clean, single-file frontend interface featuring:
  * ☀️ / 🌙 **Dark & Light Mode** toggle.
  * Real-time system telemetry and latency indicators.
  * Interactive suggested query chips.
  * Document source attribution pills for answers.
* **FastAPI Backend:** Lightweight RESTful API endpoints for system status and query execution with interactive Swagger UI documentation at `/docs`.

---

## 🏗️ Project Architecture

```text
enterprise_rag_bot/
├── data/                      # Directory containing corporate text documents (.txt)
│   └── sample_policy.txt      # Example policy document
├── app.py                     # FastAPI web server and routing
├── rag_engine.py              # Vector indexing, chunking, and Gemini RAG pipeline
├── test_rag.py                # Standalone CLI test script
├── index.html                 # Futuristic web UI frontend
└── README.md                  # Project documentation

## 🚀 Quick Start Guide

### 1. Prerequisites

Ensure you have **Python 3.11+** installed on your machine.

### 2. Environment Setup

Clone the repository and navigate into the project folder:

```bash
git clone [https://github.com/your-username/enterprise-policy-rag-bot.git](https://github.com/your-username/enterprise-policy-rag-bot.git)
cd enterprise-policy-rag-bot

Install the required Python dependencies:

Bash
pip install fastapi uvicorn google-genai sentence-transformers numpy pydantic



API Key Configuration

Obtain a Google Gemini API Key from Google AI Studio.

Set your API key in your terminal session:

PowerShell (Windows):

PowerShell
$env:GEMINI_API_KEY="your_api_key_here"
Bash / Linux / macOS:

Bash
export GEMINI_API_KEY="your_api_key_here"
Note: Alternatively, you can configure your API key directly within rag_engine.py.

4. Running the Application
Start the FastAPI server with uvicorn:

Bash
uvicorn app:app --reload
Open your browser and visit:

Web UI Console: http://127.0.0.1:8000

Swagger API Docs: http://127.0.0.1:8000/docs

🧪 Testing the CLI RAG Engine
You can test document loading, semantic embedding search, and LLM generation directly via the terminal script:

Bash
python test_rag.py
Example Output:
Plaintext
Initializing RAG Engine...
Querying: 'How many days of paid leave do employees get?'

--- RESPONSE ---
Answer: Employees get 20 days of paid leave annually.
Sources: ['sample_policy.txt']
🛠️ API Reference
POST /query
Submit a question to the knowledge base.

Request Body:

JSON
{
  "query": "What are the remote work approval guidelines?"
}
Response:

JSON
{
  "answer": "Remote work requires manager approval 48 hours in advance.",
  "sources": [
    "sample_policy.txt"
  ]
}
GET /
Serves index.html web dashboard or returns JSON health metrics.

📁 Adding Custom Policy Documents
Drop any corporate .txt document into the ./data/ folder.

Restart the server (uvicorn app:app --reload).

The engine automatically chunks, embeds, and indexes new documents on startup!

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.



