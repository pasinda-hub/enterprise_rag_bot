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
