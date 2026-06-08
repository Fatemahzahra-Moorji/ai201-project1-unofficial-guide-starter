import os
import re


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

HTML_ENTITIES = {
    "&amp;": "&",
    "&nbsp;": " ",
    "&lt;": "<",
    "&gt;": ">",
    "&quot;": '"',
    "&apos;": "'",
    "&#39;": "'",
    "&#x27;": "'",
}


def replace_html_entities(text):
    for entity, replacement in HTML_ENTITIES.items():
        text = text.replace(entity, replacement)
    text = re.sub(r"&#\d+;", "", text)
    return text


def clean_text(text):
    text = replace_html_entities(text)

    text = text.replace("\r\n", "\n").replace("\r", "\n")

    lines = [line.rstrip() for line in text.split("\n")]

    cleaned_lines = []
    blank_run = 0
    for line in lines:
        if line == "":
            blank_run += 1
            if blank_run <= 1:
                cleaned_lines.append(line)
        else:
            blank_run = 0
            line = re.sub(r"[ \t]+", " ", line)
            cleaned_lines.append(line)

    text = "\n".join(cleaned_lines).strip()
    return text


def load_documents(data_dir=DATA_DIR):
    documents = []

    filenames = sorted(
        f for f in os.listdir(data_dir) if f.endswith(".txt")
    )

    for filename in filenames:
        filepath = os.path.join(data_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            raw = f.read()

        cleaned = clean_text(raw)
        documents.append({"source": filename, "text": cleaned})

    return documents


if __name__ == "__main__":
    docs = load_documents()
    for doc in docs:
        print(f"--- {doc['source']} ---")
        print(doc["text"][:500])
        print()
