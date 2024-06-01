from pinecone import Pinecone
from app.config.config import settings

class PineconeClient:
    def __init__(self):
        pc = Pinecone(api_key=settings.PINECONE_API_KEY)
        self.index = pc.Index(settings.PINECONE_INDEX_NAME)

    def insert_embeddings(self, embeddings: list):
        self.index.upsert(vectors=embeddings, namespace= "ns1")

    def search(self, query_embedding: list, top_k: int = 10):
        return self.index.query(queries=[query_embedding], top_k=top_k).matches
