**Hybrid LlamaIndex + LangChain pipeline**

**LlamaIndex + LangChain Report Summarizer**

This project demonstrates how to build a data-centric AI pipeline using LlamaIndex (for ingestion & retrieval) and LangChain (for orchestration & refinement).
It ingests local documents, builds a semantic index, retrieves relevant content, and generates structured summaries saved to CSV.


**Features**

**Data Ingestion (LlamaIndex)**
Loads documents from ./data folder.
Splits and embeds them into a vector index.
Persists the index locally for reuse.

**Semantic Retrieval**
Natural language queries over reports.
Retrieves most relevant chunks using vector search.

**LLM Orchestration (LangChain)**
Refines raw retrieved text with prompt templates.
Extracts concise insights into bullet points.

**Export to CSV**
Saves summaries into report_summary.csv.
Useful for reporting, research, or dashboards.

**Project Structure**
.
├── data/                   # Place your reports (txt, pdf, docx) here
├── ingestion.py            # First-time ingestion: build & persist index
├── main.py                  # Query + summarize with LlamaIndex + LangChain
├── report_summary.csv      # Auto-generated output
├── requirements.txt
└── README.md
└── .env                    # for secret keys - not available here

