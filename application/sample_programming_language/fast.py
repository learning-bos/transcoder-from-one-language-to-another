from fastembed import TextEmbedding
from numpy import float32

documents = [
    "passage: Hello, World!",
    "query: Hello, World!",
    "passage: This is an example passage.",
    "fastembed is supported by and maintained by Qdrant."
]
embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5", )
embeddings = list(embedding_model.embed(documents))
assert len(embeddings[0]) == 384
assert type(embeddings[0][0]) == float32
print("All good")
