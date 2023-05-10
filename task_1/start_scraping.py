import json
import os
from tqdm import tqdm
from get_links import collect_urls
from get_articles import collect_text
import requests

def collect_the_data(CONSTANTS):
    """Collects all articles"""

    collect_urls(CONSTANTS)  # Collect urls and summaries

    with open(CONSTANTS["SAVE_PROGRESS"]) as f:  # Read urls and summaries
        saved_progress = json.load(f)
        urls = saved_progress["urls"]
        category = saved_progress["category"]
        headers_list = saved_progress["headers"]
        author_list = saved_progress["authors"]

    if os.path.isfile(CONSTANTS["SAVE_FILE"]):  # If save file exists, read progress from file
        with open(CONSTANTS["SAVE_FILE"]) as f:
            saved_data = json.load(f)
            start_index = saved_data.get("index", 0)
            if start_index == saved_progress["index"]:  # If we have already finished, return
                return "Already finished"
            articles = saved_data.get("articles", [])
    else:  # Otherwise, start from the beginning
        start_index = 0
        articles = []

    return collect_text(CONSTANTS, urls, category, headers_list, author_list, articles)

if __name__ == "__main__":
    # Get directory path
    curr_dir = os.path.dirname(os.path.abspath(__file__)) 
    curr_dir = curr_dir.split('/')
    curr_dir = '/'.join(curr_dir[:-1]) 
    # Define constants
    CONSTANTS = {
        "SAVE_EVERY": 30,
        "SAVE_PROGRESS": f"{curr_dir}/dataset/urls.json",
        "SAVE_FILE": f"{curr_dir}/dataset/articles.json",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; Build/KLP) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30"
        },
        "session": requests.Session(),
        "end_page": 6378,
    }

    collect_the_data(CONSTANTS)
