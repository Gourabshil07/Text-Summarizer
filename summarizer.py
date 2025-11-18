import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_summarizer():
    summarizer = pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6",   
        device=-1                                
    )
    return summarizer


def summarize_text(text):
    summarizer = load_summarizer()

    # Generate summary
    result = summarizer(
        text,
        max_length=150,
        min_length=40,
        do_sample=False
    )

    return result[0]["summary_text"]
