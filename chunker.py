import random

from langchain_text_splitters import RecursiveCharacterTextSplitter

from ingest import load_documents


CHUNK_SIZE = 300
CHUNK_OVERLAP = 50


def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    chunks = []
    for doc in documents:
        pieces = splitter.split_text(doc["text"])
        for piece in pieces:
            if len(piece.strip()) >= 100:
                chunks.append({"source": doc["source"], "text": piece})

    return chunks


if __name__ == "__main__":
    documents = load_documents()
    chunks = chunk_documents(documents)

    print(f"Total chunks: {len(chunks)}\n")

    sample = random.sample(chunks, min(5, len(chunks)))
    for i, chunk in enumerate(sample, start=1):
        print(f"--- Sample {i} | {chunk['source']} ---")
        print(chunk["text"])
        print()
