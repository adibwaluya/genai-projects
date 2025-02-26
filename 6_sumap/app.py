import validators, streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

# Streamlit config
st.set_page_config(page_title="LangChain: Summarize Text from YouTube or Website")
st.title("LangChain: Summarize Text from YouTube or Website")
st.subheader('Summarize URL')

# UI for Groq API key & url/youtube links
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value = "", type="password")

url = st.text_input("URL", label_visibility="collapsed")

