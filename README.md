<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=24&duration=2500&pause=1000&color=00F0FF&center=true&vCenter=true&width=800&height=50&lines=⚡+ENTERPRISE+POLICY+RAG+ASSISTANT;🔒+NEURAL+KNOWLEDGE+RETRIEVAL+SYSTEM;🚀+AI-POWERED+COMPLIANCE+ENGINE" />
</p>

<!-- ANIMATED VECTOR CYBERPUNK BACKGROUND BANNER -->
<p align="center">
  <svg width="100%" height="180" viewBox="0 0 900 180" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <!-- Deep Cyberpunk Dark Gradient -->
      <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#050510" />
        <stop offset="50%" stop-color="#0B091A" />
        <stop offset="100%" stop-color="#12041D" />
      </linearGradient>

      <!-- Neon Text Gradient -->
      <linearGradient id="text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00F0FF" />
        <stop offset="50%" stop-color="#7000FF" />
        <stop offset="100%" stop-color="#FF0055" />
      </linearGradient>

      <!-- Glow Filter -->
      <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="5" result="blur" />
        <feComposite in="SourceGraphic" in2="blur" operator="over" />
      </filter>
    </defs>

    <!-- Background Base -->
    <rect width="900" height="180" rx="14" fill="url(#bg-grad)" stroke="#00F0FF" stroke-width="1.5" stroke-opacity="0.5" />

    <!-- MOVING VECTOR GRID LINES -->
    <g stroke="#00F0FF" stroke-opacity="0.1" stroke-width="1">
      <line x1="0" y1="45" x2="900" y2="45" />
      <line x1="0" y1="90" x2="900" y2="90" />
      <line x1="0" y1="135" x2="900" y2="135" />
      
      <!-- Animated vertical data stream lines -->
      <line x1="150" y1="0" x2="150" y2="180" stroke-dasharray="5 15">
        <animate attributeName="stroke-dashoffset" values="100;0" dur="4s" repeatCount="indefinite" />
      </line>
      <line x1="450" y1="0" x2="450" y2="180" stroke-dasharray="8 20" stroke="#FF0055">
        <animate attributeName="stroke-dashoffset" values="0;100" dur="6s" repeatCount="indefinite" />
      </line>
      <line x1="750" y1="0" x2="750" y2="180" stroke-dasharray="6 12" stroke="#00FF66">
        <animate attributeName="stroke-dashoffset" values="100;0" dur="5s" repeatCount="indefinite" />
      </line>
    </g>

    <!-- FLOATING VECTOR DATA NODES (ANIMATED) -->
    <g filter="url(#glow)">
      <!-- Node 1 -->
      <circle cx="100" cy="50" r="3.5" fill="#00F0FF">
        <animate attributeName="cy" values="45;65;45" dur="3s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0.3;1;0.3" dur="3s" repeatCount="indefinite" />
      </circle>
      <!-- Node 2 -->
      <circle cx="820" cy="120" r="4" fill="#FF0055">
        <animate attributeName="cy" values="120;100;120" dur="4s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0.4;1;0.4" dur="4s" repeatCount="indefinite" />
      </circle>
      <!-- Node 3 -->
      <circle cx="700" cy="40" r="3" fill="#00FF66">
        <animate attributeName="cx" values="700;720;700" dur="5s" repeatCount="indefinite" />
      </circle>
      <!-- Node 4 -->
      <small><circle cx="200" cy="140" r="3" fill="#00F0FF" /></small>
    </g>

    <!-- MAIN BANNER TITLE -->
    <text x="50%" y="82" font-family="'Fira Code', 'Segoe UI', monospace" font-weight="900" font-size="34" fill="url(#text-grad)" text-anchor="middle" filter="url(#glow)">
      Enterprise Policy RAG Assistant
    </text>

    <!-- SUBTITLE TECH STATUS -->
    <text x="50%" y="125" font-family="'Fira Code', 'Segoe UI', monospace" font-weight="600" font-size="13" fill="#00FF66" text-anchor="middle" letter-spacing="5">
      [ VECTOR KNOWLEDGE BASE // LIVE NEURAL STREAM ]
    </text>
  </svg>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/ARCHITECTURE-RAG_HYBRID-00F0FF?style=for-the-badge&logo=openai&logoColor=black" />
  <img src="https://img.shields.io/badge/SECURITY-ENTERPRISE_GRADE-FF0055?style=for-the-badge&logo=shield&logoColor=white" />
  <img src="https://img.shields.io/badge/LATENCY-%3C150ms-00FF66?style=for-the-badge&logo=lightning&logoColor=black" />
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
