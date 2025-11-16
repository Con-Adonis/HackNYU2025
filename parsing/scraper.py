import json
from .cnbc import scrape as scrape_cnbc
from .novanews import scrape as scrape_nova


def run_all():
    # For now we only have CNBC + NovaNews, but this could easily be extended.
    articles = {
        "NovaNews": scrape_nova(),
    }

    # Try CNBC but don't crash if it fails
    try:
        articles["CNBC"] = scrape_cnbc()
    except Exception as e:
        print("CNBC scrape failed:", e)
        articles["CNBC"] = None

    return articles


if __name__ == "__main__":
    # If we run this file directly, just scrape and dump everything to JSON
    # so we can inspect it or test scraping without the Gemini part.
    articles = run_all()

    # Save the combined results for Connor
    with open("data/articles.json", "w") as f:
        json.dump(articles, f, indent=4)

    print("Scraping complete. Saved → data/articles.json")
