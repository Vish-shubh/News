import streamlit as st
from utils import scrape_news, analyze_sentiment, comparative_analysis, generate_hindi_tts

st.title("News Summarization and Sentiment Analysis")

company_name = st.text_input("Enter Company Name")
if st.button("Analyze"):
    articles = scrape_news(company_name)
    for article in articles:
        article["sentiment"] = analyze_sentiment(article["summary"])
    sentiment_counts = comparative_analysis(articles)
    st.write(sentiment_counts)
    tts_file = generate_hindi_tts("Summary of sentiment analysis")
    st.audio(tts_file)