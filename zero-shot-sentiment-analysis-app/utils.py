import streamlit as st

def load_openai_key():
    # Try to get key from Streamlit secrets first
    key = st.secrets.get("OPENAI_API_KEY", None)
    if key is None:
        raise ValueError("OpenAI API key not found in Streamlit secrets.")
    assert key.startswith('sk-'), "Invalid OpenAI API key format."
    return key