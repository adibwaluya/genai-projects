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

generic_url = st.text_input("URL", label_visibility="collapsed")

## Gemma model
llm = ChatGroq(model = "Gemma-7b-It", groq_api_key = groq_api_key)

if st.button("Summarize the content from YouTube or Website"):

    # validate input
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL. It ca be a YouTube or website link")

    else:
        try:
            with st.spinner("Waiting..."):

                # load the site or youtube data
                if "youtube.com" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info = True)
                else:
                    loader = UnstructuredURLLoader(
                        urls = [generic_url],
                        ssl_verify = False,
                        headers = {
                            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
                        }
                    )
                docs = loader.load()

               
        except: