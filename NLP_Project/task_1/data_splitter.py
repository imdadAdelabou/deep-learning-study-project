import pandas as pd
import os

def split_data(file_path, output_path):
    df = pd.read_json(file_path)
    categories = df["category"].unique()
    for category in categories:
        df[df["category"] == category].to_json(f"{output_path}{category}.json", orient="records")
    return "Data split and saved to JSON files"

if __name__ == "__main__":
    # Get directory path
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    curr_dir = curr_dir.rsplit("/", 1)[0]
    file_path = f"{curr_dir}/dataset/articles_clean.json"
    output_path = f"{curr_dir}/dataset_by_category/"
    os.mkdir(output_path) if not os.path.exists(output_path) else None # Create directory if not exists
    # Split data
    print(split_data(file_path, output_path))
