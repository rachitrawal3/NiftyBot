import streamlit as st
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Nifty 50 mapping
company_map = {
    "adani enterprises": "ADANIENT",
    "adani ports": "ADANIPORTS",
    "apollo hospitals": "APOLLOHOSP",
    "asian paints": "ASIANPAINT",
    "axis bank": "AXISBANK",
    "bajaj auto": "BAJAJ-AUTO",
    "bajaj finance": "BAJFINANCE",
    "bajaj finserv": "BAJAJFINSV",
    "bharat electronics": "BEL",
    "bharti airtel": "BHARTIARTL",
    "cipla": "CIPLA",
    "coal india": "COALINDIA",
    "dr reddy's laboratories": "DRREDDY",
    "eicher motors": "EICHERMOT",
    "grasim industries": "GRASIM",
    "hcl technologies": "HCLTECH",
    "hdfc bank": "HDFCBANK",
    "hdfc life": "HDFCLIFE",
    "hero motocorp": "HEROMOTOCO",
    "hindalco industries": "HINDALCO",
    "hindustan unilever": "HINDUNILVR",
    "icici bank": "ICICIBANK",
    "indusind bank": "INDUSINDBK",
    "infosys": "INFY",
    "itc": "ITC",
    "jio financial services": "JIOFIN",
    "jsw steel": "JSWSTEEL",
    "kotak mahindra bank": "KOTAKBANK",
    "larsen & toubro": "LT",
    "mahindra & mahindra": "M&M",
    "maruti suzuki": "MARUTI",
    "nestle india": "NESTLEIND",
    "ntpc": "NTPC",
    "oil and natural gas corporation": "ONGC",
    "power grid": "POWERGRID",
    "reliance industries": "RELIANCE",
    "sbi life insurance": "SBILIFE",
    "shriram finance": "SHRIRAMFIN",
    "state bank of india": "SBIN",
    "sun pharma": "SUNPHARMA",
    "tata consultancy services": "TCS",
    "tata consumer products": "TATACONSUM",
    "tata motors": "TATAMOTORS",
    "tata steel": "TATASTEEL",
    "tech mahindra": "TECHM",
    "titan company": "TITAN",
    "trent": "TRENT",
    "ultratech cement": "ULTRACEMCO",
    "wipro": "WIPRO",
    "zomato": "ETERNAL"
}

def get_symbol(user_input):
    user_input = user_input.strip().lower()
    return company_map.get(user_input, user_input.upper())

# Streamlit UI
st.title("NIFTYBOT")

user_query = st.text_input("Enter a company name (e.g., Reliance, TCS, Infosys):")

if user_query:
    symbol = get_symbol(user_query)

    url_nse = f"https://www.screener.in/company/{symbol}/consolidated/"
    url_yahoo = f"https://finance.yahoo.com/quote/{symbol}.NS/news/"
    st.write(f"Fetching data from: {url_nse}")
    st.write(f"Fetching data from: {url_yahoo}")

    try:
        docs_nse = WebBaseLoader(url_nse).load()
        docs_yahoo = WebBaseLoader(url_yahoo).load()
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.stop()

    docs = docs_nse + docs_yahoo
    docs = docs[:50]

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model="moondream")
    vectorstore = FAISS.from_documents(docs, embeddings)

    llm = ChatGroq(groq_api_key=groq_api_key, model_name="gemma2-9b-it")

    custom_prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a smart financial advisor AI assistant.give a brief sarcastic disclaimer and then Use the following extracted context (from news and financial websites) to answer the user's question.
Your task is to give a clear, opinionated investment suggestion based on current news and company fundamentals.

Context:
{context}

Question:
{question}

Answer with clear reasoning, key risks, and final verdict (invest, hold, or avoid).In the end also tell the alternative investment options if any in the same domain of asked stock.
"""
    )

    # Use the custom prompt
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": custom_prompt}
    )

    # Use a clear question for better context
    final_question = f"Should I invest in {user_query.title()}?"
    answer = qa.run(final_question)

    st.subheader("Investment Opinion:")
    st.write(answer)

