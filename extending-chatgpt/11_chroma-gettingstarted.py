# https://docs.trychroma.com/getting-started
import chromadb
chroma_client = chromadb.Client()

# No embedding_function provided, using default embedding function: 
# DefaultEmbeddingFunction https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
collection = chroma_client.create_collection(name="my_collection")

collection.add(
    documents=["This is a document", "This is another document"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
)


# If you have already generated embeddings yourself, you can load them directly in:
# collection.add(
#     embeddings=[[1.2, 2.3, 4.5], [6.7, 8.2, 9.2]],
#     documents=["This is a document", "This is another document"],
#     metadatas=[{"source": "my_source"}, {"source": "my_source"}],
#     ids=["id1", "id2"]
# )

results = collection.query(
    query_texts=["This is a query document"],
    n_results=2
)

print(results)