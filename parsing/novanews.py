from selenium.webdriver.common.by import By
from .driver import get_driver
import time
import json

def scrape():
    driver = get_driver()

    url = "https://portfolio-news-mock.vercel.app/article.html"
    driver.get(url)
    time.sleep(1.5)

    try:
        meta_raw = driver.find_element(By.ID, "article-raw-meta").text
        meta = json.loads(meta_raw)
    except Exception:
        meta = {
            "title": "(Untitled)",
            "date": "Unknown",
            "publisher": "Fahmy Macro Wire",
            "editors": "N/A",
            "tickers": "N/A",
            "sentiment": "N/A",
        }

    try:
        paragraphs = driver.find_elements(By.CSS_SELECTOR, "#article-content p")
        content = "\n".join(p.text for p in paragraphs if p.text.strip())
    except Exception:
        content = "N/A"

    driver.quit()

    # Normalize everything into a dict so the rest of the pipeline doesn't
    # care where it came from (NovaNews vs CNBC, etc.).
    return {
        "headline": meta.get("title", ""),
        "subheader": "",
        "date": meta.get("date", ""),
        "publisher": meta.get("publisher", ""),
        "writers": [meta.get("editors", "")],
        "tickers": meta.get("tickers", ""),
        "sentiment": meta.get("sentiment", ""),
        "content": content,
    }
