# from pymilvus import connections, Collection, CollectionSchema, FieldSchema, DataType
# from app.config.config import settings

# class MilvusClient:
#     def __init__(self):
#         connections.connect("default", host=settings.MILVUS_HOST, port=settings.MILVUS_PORT)
#         self.collection_name = "document_embeddings"
#         self._create_collection()

#     def _create_collection(self):
#         if not self.collection_name in connections.get_connection().list_collections():
#             fields = [
#                 FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),
#                 FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=768)  # Adjust dimension as necessary
#             ]
#             schema = CollectionSchema(fields)
#             self.collection = Collection(self.collection_name, schema)
#         else:
#             self.collection = Collection(self.collection_name)

#     def insert_embeddings(self, embeddings):
#         self.collection.insert(embeddings)
#         self.collection.flush()

#     def search(self, embedding, top_k=5):
#         search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
#         results = self.collection.search([embedding], "embedding", search_params, limit=top_k)
#         return results
