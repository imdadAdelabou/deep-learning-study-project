import json
import time
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def collect_text(CONSTANTS, article_urls, category, headers_list, author_list, articles):
    """Collects text from the urls"""
    for i, url in tqdm(enumerate(article_urls), total=len(article_urls)):
        index = i
        retry = True
        max_retries = 3

        while retry and max_retries > 0:
            try:
                resp = CONSTANTS["session"].get(url, headers=CONSTANTS["headers"])
                retry = False
            except (requests.exceptions.RequestException, ConnectionError, TimeoutError):
                # Wait for 5 seconds and try again
                time.sleep(5)
                max_retries -= 1

        if max_retries == 0:
            print(f"Failed to retrieve {url}")
            continue

        soup = BeautifulSoup(resp.content, "lxml")

        article = {
            "url": url,
            "category": category[index],
            "header": headers_list[index],
            "author": author_list[index],
        }
        try:
            article["article_text"] = soup.find("div", class_="entry-content").get_text(strip=True)
        except:
            article["article_text"] = None

        try:
            article["date"] = soup.find("time", class_="entry-date published").get_text(strip=True)
        except:
            article["date"] = None

        articles.append(article)
        time.sleep(0.1)

        # Save progress every SAVE_EVERY steps or at the end
        if i % CONSTANTS["SAVE_EVERY"] == 0 or i >= len(article_urls) - CONSTANTS["SAVE_EVERY"]:
            with open(CONSTANTS["SAVE_FILE"], "w+", encoding="UTF-8") as f:
                data = {"index": index, "articles": articles}
                json.dump(data, f)

    return "Done"
