import pandas as pd
import torch
from torch.utils.data import DataLoader
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from tqdm import tqdm
import os


def create_QA(file_path, output_path):
    df = pd.read_json(file_path)  # read JSON file
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    tokenizer = AutoTokenizer.from_pretrained("potsawee/t5-large-generation-squad-QuestionAnswer")
    model = AutoModelForSeq2SeqLM.from_pretrained("potsawee/t5-large-generation-squad-QuestionAnswer")
    model.to(device)

    df['question'] = None
    df['answer'] = None

    # Create separate lists for questions and answers
    questions = []
    answers = []

    # Create a DataLoader for efficient batching and parallel processing
    data_loader = DataLoader(df["article_text"], batch_size=16, shuffle=False)

    for batch in tqdm(data_loader):
        # Tokenize the batch of input sequences
        inputs = tokenizer.batch_encode_plus(
            batch,
            padding="longest",
            truncation=True,
            max_length=512,
            return_tensors="pt"
        ).to(device)

        # Generate question-answer pairs for the batch
        with torch.no_grad():
            outputs = model.generate(**inputs, max_length=512)

        # Decode the generated outputs
        decoded_outputs = tokenizer.batch_decode(outputs, skip_special_tokens=False)

        # Split the decoded outputs into question and answer pairs
        for output in decoded_outputs:
            output = output.replace(tokenizer.pad_token, "").replace(tokenizer.eos_token, "")
            qa_pair = output.split(tokenizer.sep_token)
            question = qa_pair[0]
            answer = qa_pair[1]
            questions.append(question)
            answers.append(answer)

    # Assign the generated question-answer pairs to the DataFrame
    df["question"] = questions
    df["answer"] = answers

    df.to_json(output_path, orient="records", force_ascii=False)  # save to JSON file
    return "Q&A created and saved to JSON file"


if __name__ == "__main__":
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    curr_dir = curr_dir.rsplit("/", 1)[0]
    file_path = f"{curr_dir}/dataset/articles_clean.json"
    output_path = f"{curr_dir}/dataset/articles_clean_QA.json"
    # Clean data
    print(create_QA(file_path, output_path))
