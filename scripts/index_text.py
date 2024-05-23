import os
from haystack.document_store.elasticsearch import ElasticsearchDocumentStore
from haystack.nodes import PreProcessor

document_store = ElasticsearchDocumentStore(host="localhost", username="", password="", index="manuals")

processed_dir = "data/processed"

docs = []
for file in os.listdir(processed_dir):
    if file.endswith(".txt"):
        with open(os.path.join(processed_dir, file), "r") as f:
            text = f.read()
            docs.append({"content": text, "meta": {"name": file}})

document_store.write_documents(docs)
