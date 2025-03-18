
from bs4 import BeautifulSoup
import requests
from transformers import pipeline
from gtts import gTTS


def scrape_news(company_name):
    url = f"https://news.google.com/search?q={company_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    for item in soup.find_all('article')[:10]:  # Limit to 10 articles
        title = item.find('a', class_='DY5T1d').text
        link = "https://news.google.com" + item.find('a', class_='DY5T1d')['href']
        summary = item.find('div', class_='xBbh9').text if item.find('div', class_='xBbh9') else ""
        articles.append({"title": title, "link": link, "summary": summary})
    return articles


def analyze_sentiment(text):
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)[0]
    return result['label']


def comparative_analysis(articles):
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for article in articles:
        sentiment_counts[article["sentiment"]] += 1
    return sentiment_counts

def generate_hindi_tts(text, filename="output.mp3"):
    tts = gTTS(text, lang='hi')
    tts.save(filename)
    return filename

