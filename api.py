from fastapi import FastAPI
from utils import scrape_news, analyze_sentiment

app = FastAPI()

@app.get("/analyze/{company_name}")
def analyze_company(company_name: str):
    articles = scrape_news(company_name)
    for article in articles:
        article["sentiment"] = analyze_sentiment(article["summary"])
    return articles