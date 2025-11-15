
#Individual scrape function with content below:

# Headline
# Subheader
# Publication date
# Writers
# Content text

from selenium.webdriver.common.by import By
from .driver import get_driver
import time



def scrape():

    driver = get_driver()

    #Go to CNBC markets page

    driver.get("https://www.cnbc.com/markets/")
    time.sleep(2)

    #Click the first article card

    first = driver.find_element(By.CSS_SELECTOR, "a.Card-title")
    url = first.get_attribute("href")

    driver.get(url)
    time.sleep(2)


        # HEADLINE 
    headline = driver.find_element(By.CSS_SELECTOR, "h1.ArticleHeader-headline").text

        #SUBHEADER
    try:
        subheader = driver.find_element(By.CSS_SELECTOR, ".ArticleHeader-dek").text
    except:
        subheader = ""

    #DATE
    date = driver.find_element(By.CSS_SELECTOR, "time[data-testid='published-timestamp']").get_attribute("datetime")

    #WRITERS
    writers = [el.text for el in driver.find_elements(By.CSS_SELECTOR, ".Author-authorName")]
    if not writers:
        writers = ["CNBC Staff"]
    #CONTENT
    paragraphs = driver.find_elements(By.CSS_SELECTOR, ".ArticleBody-articleBody p")
    content = "\n".join(p.text for p in paragraphs if p.text.strip())

    driver.quit()

    return {
            "headline": headline,
            "subheader": subheader,
            "date": date,
            "writers": writers,
            "content": content
        }


