import streamlit as st

st.set_page_config(page_title = "Multipage GenAI Application", layout = "wide")
st.title("Welcome to Multipage GenAI Application!")
st.sidebar.success("Select a page above")

# Optionally, include some general information or instructions here
st.write("""
This multi-page application allows you to interact with two different AI tools:
1. Conversational RAG with PDF Upload and Chat History
2. Summarize Contents from YouTube or Websites

Use the sidebar to navigate between applications.
""")