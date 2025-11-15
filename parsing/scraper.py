#Scraping the data from news articles, collecting libraries
import json
from .cnbc import scrape as scrape_cnbc

#Final function to run all subscrape_news functions 
def run_all():
    return {
        "CNBC": scrape_cnbc(),
    }

if __name__ == "__main__":
    articles = run_all()

    #For Connor -> save to JSON file, no strings
    with open("../data/article.json", "w") as f:
        json.dump(articles, f, indent = 4)

    print("Scraping complete. See output in data/article.json")

