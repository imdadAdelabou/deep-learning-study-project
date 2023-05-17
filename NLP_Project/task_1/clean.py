import os
import pandas as pd
import json

def clean_text(text):
    text = text[:-7]  # remove "Related" at the end of each article
    text = text.replace("\n", " ").replace("\r", " ").replace("\t", " ")
    return text


def clean_data(file_path, output_path):
    f = open(file_path, encoding='utf-8')
    data = json.load(f)
    df = pd.DataFrame(data['articles'])  # convert to DataFrame
    df["article_text"] = df["article_text"].apply(clean_text)  # clean text
    df.to_json(output_path, orient="records")  # save to JSON file
    return "Data cleaned and saved to JSON file"


if __name__ == "__main__":
    # Get directory path
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    curr_dir = curr_dir.rsplit("/", 1)[0]
    file_path = f"{curr_dir}/dataset/articles.json"
    output_path = f"{curr_dir}/dataset/articles_clean.json"
    # Clean data
    print(clean_data(file_path, output_path))
