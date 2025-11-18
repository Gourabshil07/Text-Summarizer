import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="Text Summarizer", layout="centered")

st.title("📄 Text Summarizer")
st.write("Paste your text or upload a pdf file to generate a concise summary",height=30)

# Text input
text_area = st.text_area("✏️ Paste your text here:", height=250,background_color="#D78B09")


# Button
if st.button("🔍 Analyze"):
    if not text_area.strip():
        st.warning("Please paste or upload text first!")
    else:
        with st.spinner("Summarizing..."):
            summary = summarize_text(text_area)

        st.subheader("🧠 Summary:")
        st.write(summary)

        st.download_button(
            label="⬇️ Download Summary",
            data=summary,
            file_name="summary.txt"
        )
