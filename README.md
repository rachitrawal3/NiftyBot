📈 NiftyBot – AI-Powered Investment Opinion Chatbot for NIFTY 50
NiftyBot is an intelligent, real-time investment advisory chatbot built using LangChain, FAISS, Streamlit, and Groq LLMs. This tool provides clear, context-aware, and opinionated financial suggestions about companies listed in the NIFTY 50 index based on the latest scraped data from sources like Screener.in and Yahoo Finance.

Whether you're an investor, finance student, or just curious about the markets, NiftyBot makes it fun and insightful to evaluate Indian blue-chip stocks.

💡 Features
🔍 Smart Company Mapping: Automatically maps user input to the correct NIFTY 50 stock symbol (e.g., "reliance" → RELIANCE).

🌐 Live Web Scraping: Pulls the latest data and news from:

Screener.in

Yahoo Finance India

📄 Chunked Text Analysis: Breaks down scraped data into meaningful chunks using RecursiveCharacterTextSplitter for better context understanding.

🧠 RAG-based QA System: Combines context retrieval (via FAISS) and reasoning (via Groq's gemma2-9b-it) to give intelligent advice.

🗣️ Opinionated Answering: Provides:

Sarcastic disclaimer 😅

Financial reasoning

Key risks

Final verdict: Invest, Hold, or Avoid

Alternative investment suggestions in the same domain

🖥️ Clean UI: Simple and interactive frontend built using Streamlit.

🧱 Tech Stack
Technology	Purpose
Streamlit	Frontend UI for user interaction
LangChain	Managing prompts and retrieval chain
FAISS	Vector-based document search
Ollama Embeddings	For embedding web content into vectors
ChatGroq	Fast LLM backend (using gemma2-9b-it)
WebBaseLoader	For scraping data from web URLs
⚙️ How It Works
User enters a company name.

The app maps it to the correct NIFTY 50 stock symbol.

Scrapes latest financials and news headlines.

Splits data into chunks and embeds using Ollama.

Uses LangChain's RetrievalQA with a custom prompt to generate an informed, sarcastic-yet-serious response.

Displays a final investment opinion with suggested alternatives.  
