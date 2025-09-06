import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import StorageContext,load_index_from_storage

from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI as LangOpenAI 
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Please set your OPENAI_API_KEY environment variable.")



#VectorStoreIndex.from_documents() → for first-time ingestion.
#index.storage_context.persist() → saves it to disk.
#load_index_from_storage(storage_context) → reloads the same index later without re-embedding.


# Load existing index
storage_context = StorageContext.from_defaults(persist_dir="index__loc_storage")
index = load_index_from_storage(storage_context)  

query_engine = index.as_query_engine() 

# User Query 
user_query = "Summarize key findings across the reports and list them in bullets"

# Step 1: Retrieve relevant info using LlamaIndex
retrieved_info = query_engine.query(user_query)
 
summary = str(retrieved_info)

# Langchain in picture -- 
# Step 2: Refine & Structure with LangChain
prompt_template = """You are an AI research assistant.
Here is the retrieved information:
{doc_summary} 
Extract 3 key insights in bullet points and make it concise."""

prompt = PromptTemplate(template=prompt_template, input_variables=["doc_summary"])

lang_llm = LangOpenAI(
    model="gpt-4o-mini",  
    temperature=0,
    openai_api_key=OPENAI_API_KEY
)

chain = LLMChain(prompt=prompt, llm=lang_llm)

final_output = chain.run(doc_summary=summary)

# ------------------ Save Results ------------------
import pandas as pd

bullets = [b.strip() for b in final_output.split("\n") if b.strip()]
df = pd.DataFrame({"Key Insights": bullets})
df.to_csv("report_summary.csv", index=False)

print("✅ Summary generated and saved as report_summary.csv")
print("\nFinal Summary:")
print(final_output)
