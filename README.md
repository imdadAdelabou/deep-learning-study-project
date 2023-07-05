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
  <li>Dataset row: 76290</li>
  <li>Mean context length: 642 words</li>
  <li>Metadata: ["URL", "Header", "Category", "Author", "Date Published", "Article Title"]</li>
</ul>

1.) Getting URLs, Extracting Metadata and texts
<ul>
  <li>run pip install -r requirements.txt</li>
  <li>run start_scraping.py - # Written by Rostislav Manakov - Scraped urls and articles</li>
  <li>run data_cleaner.py - # Written by Imdad Adelabou - Removes unwanted symbols from the scraped datasets texts</li>
  <li>run data_splitter.py - # Written by Rostislav Manakov - Splits the dataset into multiple files based on date of publication</li>
</ul>

2.) Creating Q&A pairs
<ul>
  <li>run pcreate_Q&A.py # Written by Rostislav Manakov, Imdad Adelabou - Creates quastion-answer pairs using: </li>
  <li>potsawee/t5-large-generation-squad-QuestionAnswer</li>
</ul>

3.) Prepare data for Evaluation
<ul>
  <li>if you created Answers from medium-sized language models correctly this step may be unnecesary</li>
  <li>run clean_dataset.py - # Written by Rostislav Manakov</li>
</ul>
