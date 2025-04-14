

# 📈 NiftyBot – AI-Powered Investment Opinion Chatbot for NIFTY 50

**NiftyBot** is an intelligent, real-time investment advisory chatbot built using **LangChain**, **FAISS**, **Streamlit**, and **Groq LLMs**. This tool provides **clear, context-aware, and opinionated financial suggestions** about companies listed in the **NIFTY 50** index based on the latest scraped data from sources like **Screener.in** and **Yahoo Finance**.

Whether you're an investor, finance student, or just curious about the markets, **NiftyBot** makes it fun and insightful to evaluate Indian blue-chip stocks.

---

## 💡 Features

- 🔍 **Smart Company Mapping**: Automatically maps user input to the correct NIFTY 50 stock symbol (e.g., "reliance" → `RELIANCE`).
- 🌐 **Live Web Scraping**: Pulls the latest data and news from:
  - [Screener.in](https://www.screener.in/)
  - [Yahoo Finance India](https://finance.yahoo.com/)
- 📄 **Chunked Text Analysis**: Breaks down scraped data into meaningful chunks using `RecursiveCharacterTextSplitter` for better context understanding.
- 🧠 **RAG-based QA System**: Combines context retrieval (via `FAISS`) and reasoning (via `Groq`'s `gemma2-9b-it`) to give intelligent advice.
- 🗣️ **Opinionated Answering**: Provides:
  - Sarcastic disclaimer 😅
  - Financial reasoning
  - Key risks
  - Final **verdict**: _Invest_, _Hold_, or _Avoid_
  - Alternative investment suggestions in the same domain
- 🖥️ **Clean UI**: Simple and interactive frontend built using **Streamlit**.

---

## 🧱 Tech Stack

| Technology        | Purpose                                  |
|-------------------|-------------------------------------------|
| `Streamlit`       | Frontend UI for user interaction          |
| `LangChain`       | Managing prompts and retrieval chain      |
| `FAISS`           | Vector-based document search              |
| `Ollama Embeddings` | For embedding web content into vectors |
| `ChatGroq`        | Fast LLM backend (using `gemma2-9b-it`)   |
| `WebBaseLoader`   | For scraping data from web URLs           |

---

## ⚙️ How It Works

1. User enters a company name.
2. The app maps it to the correct NIFTY 50 stock symbol.
3. Scrapes latest financials and news headlines.
4. Splits data into chunks and embeds using Ollama.
5. Uses LangChain's **RetrievalQA** with a custom prompt to generate an informed, sarcastic-yet-serious response.
6. Displays a final **investment opinion** with suggested alternatives.

---



