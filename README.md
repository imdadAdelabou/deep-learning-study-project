# Deep Learning study project
**Website choice:** https://scienceblog.com/ <br>
**Rationale:** the selected website meets all the requirements of the assignment and focuses on science.

<br />
robots.txt
<br />--- <br/>
User-Agent: * <br />
Disallow: /wp-content/plugins/ <br />
Sitemap: https://scienceblog.com/sitemap_index.xml <br />
---

### Dataset Overview:
<ul>
  <li>Dataset row: 8435</li>
  <li>Mean context length: 765 words</li>
  <li>Metadata: ["URL", "Category", "Author", "Date Published", "Article Title"]</li>
</ul>

1.) Getting URLs, Extracting Metadata and texts
<ul>
  <li>run pip install -r requirements.txt</li>
  <li>run start_scraping.py - # Written by Rostislav Manakov - Scraped urls and articles</li>
  <li>run data_cleaner.py - # Written by Imdad Adelabou - Removes unwanted symbols from the scraped datasets texts</li>
</ul>
