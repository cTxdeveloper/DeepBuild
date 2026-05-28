import chromadb
from deepbuild.config.settings import settings


class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=settings.chroma_path)
        self.collection = self.client.get_or_create_collection('deepbuild_memory')

    def add_memory(self, memory_id: str, content: str):
        self.collection.add(documents=[content], ids=[memory_id])

    def search(self, query: str, limit: int = 5):
        return self.collection.query(query_texts=[query], n_results=limit)
