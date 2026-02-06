# Basic memory 
import asynco
import chromadb
import os
from dotenv import load_dotenv; load_dotrenv()

chroma_client = chromadb.PersistentClient(path="/memory")

if "CHROMADB_COLLECTION_NAME" in os.environ:
    collection = chroma_client.create_collection(name=os.getenv("CHROMADB_COLLECTION_NAME"))
else:
    raise KeyError("CHROMADB_COLLECTION_NAME is missing. Please set it in your .env file.")

async def add_memory(document: list[str], metadata: list[dist]):
    await collection.add(
        documents=document,
        metadata = metadata
    )
    return {"status": "memory updated!"}

async def query_memory(query: list[str], where: dict | None = None):
    results = await collection.query(
        query_texts=query,
        n_results=2,
        where=where  # filter by metadata
    )
    return results

