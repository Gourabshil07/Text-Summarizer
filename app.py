import streamlit as st
from summarizer import summarize_text

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Text Summarizer",
    layout="centered"
)

# ---------------- TITLE ----------------
st.title("📄 Text Summarizer")
st.write(
    "Paste your English text below to generate a concise summary using NLP."
)

# ---------------- OPTIONAL STYLE (SAFE) ----------------
st.markdown(
    """
    <style>
    textarea {
        background-color: #F5F7FA !important;
        color: #000000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- TEXT INPUT ----------------
text_area = st.text_area(
    "✏️ Paste your text here:",
    height=250
)

# ---------------- ACTION BUTTON ----------------
if st.button("🔍 Analyze"):
    if not text_area.strip():
        st.warning("Please paste text first!")
    else:
        with st.spinner("Summarizing using NLP..."):
            summary = summarize_text(text_area)

        st.subheader("🧠 Summary:")
        st.write(summary)

        st.download_button(
            label="⬇️ Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )
