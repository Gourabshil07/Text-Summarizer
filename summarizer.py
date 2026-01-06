from transformers import pipeline

# Load NLP summarization model once
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

def summarize_text(text):
    result = summarizer(
        text,
        max_length=120,
        min_length=40,
        do_sample=False
    )
    return result[0]["summary_text"]
