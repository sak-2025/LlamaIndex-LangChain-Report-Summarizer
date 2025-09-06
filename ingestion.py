from llama_index.core import VectorStoreIndex , SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


if not OPENAI_API_KEY:
    raise ValueError("Please set your OPENAI_API_KEY environment variable.")

# Load docs
documents = SimpleDirectoryReader("./data").load_data()
print(f"Loaded {len(documents)} of documents")

# Build index
index = VectorStoreIndex.from_documents(documents)

# model
llama_llm = OpenAI(model="gpt-4o-mini",openai_api_key=OPENAI_API_KEY)

# Save index for later use
index.storage_context.persist("index__loc_storage")

print("Ingestion complete, index saved!")