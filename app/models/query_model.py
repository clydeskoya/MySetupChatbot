from haystack.document_store.elasticsearch import ElasticsearchDocumentStore
from haystack.retriever.dense import DensePassageRetriever
from haystack.generator.transformers import RAGenerator

document_store = ElasticsearchDocumentStore(host="localhost", username="", password="", index="manuals")
retriever = DensePassageRetriever(document_store=document_store)
generator = RAGenerator(model_name_or_path="facebook/rag-token-nq")

def query_model(query):
    docs = retriever.retrieve(query)
    answer = generator.predict(query=query, documents=docs, top_k=1)
    return answer["answers"][0]["answer"]
