import json
import os
import requests
import time
from bs4 import BeautifulSoup
from tqdm import tqdm

def collect_urls(CONSTANTS):
    """Collects all urls and summaries from the website"""
    if os.path.isfile(CONSTANTS['SAVE_PROGRESS']):
        # If save file exists, read progress from file
        with open(CONSTANTS['SAVE_PROGRESS']) as f:
            saved_data = json.load(f)
            urls = saved_data['urls']
            category = saved_data['category']
            headers_list = saved_data['headers']
            author_list = saved_data['authors']
    else:
        # Otherwise, start from the beginning
        urls, category, headers_list, author_list = [], [], [], []

    for page in tqdm(range(1, CONSTANTS['end_page'])):
        page_url = f'https://scienceblog.com/page/{page}/'
        retry = True
        while retry:
            try:
                resp = CONSTANTS['session'].get(page_url, headers=CONSTANTS['headers'])
                retry = False
            except requests.exceptions.RequestException:
                # Wait for 5 seconds and try again
                time.sleep(5)
        soup = BeautifulSoup(resp.content, 'lxml')
        if not soup.find_all('div', class_='inside-article'):
            break
        blocks = soup.find_all('div', class_='inside-article')
        
        skip = False
        for block in blocks:
            url = block.find('header', class_="entry-header").a.get('href')
            if url in urls:
                # skip if the url is already present
                skip = True
                continue
            skip = False
            urls.append(url)
            try:
                category.append(block.find('footer', class_="entry-meta").a.get_text(strip=True))
            except AttributeError:
                category.append(None)
            try:
                headers_list.append(block.find('h2', class_="entry-title").get_text(strip=True))
            except AttributeError:
                headers_list.append(None)
            try:
                author_list.append(block.find('div', class_="entry-meta").get_text(strip=True))
            except:
                author_list.append(None)
        if skip == False:
            time.sleep(0.1)

        # Save progress every SAVE_EVERY steps
        if page % CONSTANTS['SAVE_EVERY'] == 0 or page >= CONSTANTS['end_page'] - CONSTANTS['SAVE_EVERY']:
            with open(CONSTANTS['SAVE_PROGRESS'], 'w+', encoding="UTF-8") as f:
                data = {
                    'urls': urls,
                    'category': category,
                    'headers': headers_list,
                    'authors': author_list,
                }
                json.dump(data, f)

    return True
