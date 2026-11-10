<!-- HEADER BANNER: DYNAMIC WAVING GRADIENT -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=0,2,5,10,20&height=220&section=header&text=PASINDA%20HUB&fontSize=50&animation=twinkle&fontColor=00F0FF" width="100%" />
</p>

<!-- ANIMATED TERMINAL TYPING EFFECT -->
<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=22&duration=2500&pause=1000&color=00FF66&center=true&vCenter=true&width=700&height=45&lines=>>+SYSTEM.INITIALIZE(%22PASINDA_CORE%22);>>+LOADING+NEURAL+RAG+BOT...;>>+TRAINING+TRAFFIC_LIGHT_RL+AGENT...;>>+STATUS%3A+ALL+SYSTEMS+OPERATIONAL" />
  </a>
</p>

<!-- SCI-FI BADGE ROW -->
<p align="center">
  <img src="https://img.shields.io/badge/CORE_OS-CYBERPUNK_V2.0-00F0FF?style=for-the-badge&logo=linux&logoColor=black" />
  <img src="https://img.shields.io/badge/CLEARANCE-LEVEL_5_ADMIN-FF0055?style=for-the-badge&logo=shield&logoColor=white" />
  <img src="https://img.shields.io/badge/NEURAL_NET-ONLINE-00FF66?style=for-the-badge&logo=openai&logoColor=black" />
</p>

---

## ⚡ // SYSTEM_CAPABILITIES & TECH_MATRIX

<p align="center">
  <!-- Languages -->
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" />
  <br>
  <!-- AI / ML & Tools -->
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
</p>

---

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

enterprise_rag_bot/
├── data/                      # Directory containing corporate text documents (.txt)
│   └── sample_policy.txt      # Example policy document
├── app.py                     # FastAPI web server and routing
├── rag_engine.py              # Vector indexing, chunking, and Gemini RAG pipeline
├── test_rag.py                # Standalone CLI test script
├── index.html                 # Futuristic web UI frontend
└── README.md                  # Project documentation

---

## 🚀 Quick Start Guide

### 1. Prerequisites

Ensure you have Python 3.11+ installed on your machine.

### 2. Environment Setup

Clone the repository and navigate into the project folder:

git clone https://github.com/your-username/enterprise-policy-rag-bot.git
cd enterprise-policy-rag-bot

Install the required Python dependencies:

pip install fastapi uvicorn google-genai sentence-transformers numpy pydantic

---

### 3. API Key Configuration

Obtain a Google Gemini API Key from Google AI Studio (https://aistudio.google.com/app/apikey).

Set your API key in your terminal session:

PowerShell (Windows):
$env:GEMINI_API_KEY="your_api_key_here"

Bash / Linux / macOS:
export GEMINI_API_KEY="your_api_key_here"

Note: Alternatively, you can configure your API key directly within rag_engine.py.

---

### 4. Running the Application

Start the FastAPI server with uvicorn:

uvicorn app:app --reload

Open your browser and visit:
* Web UI Console: http://127.0.0.1:8000
* Swagger API Docs: http://127.0.0.1:8000/docs

---

## 🧪 Testing the CLI RAG Engine

You can test document loading, semantic embedding search, and LLM generation directly via the terminal script:

python test_rag.py

Example Output:
Initializing RAG Engine...
Querying: 'How many days of paid leave do employees get?'

--- RESPONSE ---
Answer: Employees get 20 days of paid leave annually.
Sources: ['sample_policy.txt']

---

## 🛠️ API Reference

### POST /query

Submit a question to the knowledge base.

Request Body:
{
  "query": "What are the remote work approval guidelines?"
}

Response:
{
  "answer": "Remote work requires manager approval 48 hours in advance.",
  "sources": [
    "sample_policy.txt"
  ]
}

### GET /

Serves index.html web dashboard or returns JSON health metrics.

---

## 📁 Adding Custom Policy Documents

1. Drop any corporate .txt document into the ./data/ folder.
2. Restart the server (uvicorn app:app --reload).
3. The engine automatically chunks, embeds, and indexes new documents on startup!

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
