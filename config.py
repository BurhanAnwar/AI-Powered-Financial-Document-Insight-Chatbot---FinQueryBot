from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VECTOR_TYPE = os.getenv("VECTOR_TYPE", "faiss")
PG_CONN = os.getenv("PG_CONN", "")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "fin_reports")
