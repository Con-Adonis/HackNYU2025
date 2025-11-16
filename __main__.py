import os
import logic.portfolioEffect as portfolioEffect
from dotenv import load_dotenv
from parsing.scraper import run_all
import time
import logic.welcome as welcome

PORTFOLIO_GLOBAL: list[str] = []  # tickers for this run


def config():
    load_dotenv(override=True)
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        portfolio_tickers = os.getenv("PORTFOLIO_TICKERS")
        portfolio_list = [ticker.strip() for ticker in portfolio_tickers.split(",")]
    except Exception as e:
        print("Error loading configuration from .env file:", e)
        exit(1)
        
    print(api_key, portfolio_list)


def main():
    #run the setup scripts
    welcome.main()
    config()
    
    #TODO: set sleep/scrape cycle
    
    #output = portfolioEffectAnalysis()
    #print("Portfolio Effect Analysis Output:")
    #print(output)


def portfolioEffectAnalysis():
    portfolio = ", ".join(PORTFOLIO_GLOBAL) if PORTFOLIO_GLOBAL else "AAPL, MSFT, GOOGL"

    articles = run_all()

    nova_article = articles.get("NovaNews") if isinstance(articles, dict) else None
    cnbc_article = articles.get("CNBC") if isinstance(articles, dict) else None

    if nova_article and cnbc_article:
        newsTitle = f"{nova_article.get('headline', 'NovaNews')} & {cnbc_article.get('headline', 'CNBC')}"
        newsContent = (
            f"NovaNews: {nova_article.get('content', '')}\n\n"
            f"CNBC: {cnbc_article.get('content', '')}"
        )
    elif nova_article or cnbc_article:
        article = nova_article or cnbc_article
        newsTitle = article.get("headline", "Latest Market News")
        newsContent = article.get("content", "")
    else:
        newsTitle = "Apple Releases New iPhone"
        newsContent = (
            "Apple has announced the release of its latest iPhone model, which includes "
            "several new features and improvements over previous versions..."
        )

    return portfolioEffect.portfolioAnalysis(newsTitle, newsContent, portfolio)


if __name__ == "__main__":
    main()