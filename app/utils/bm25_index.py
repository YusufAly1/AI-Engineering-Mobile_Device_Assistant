
from rank_bm25 import BM25Okapi 
from app.data.devices import DEVICE_DOCUMENTS 


device_docs = DEVICE_DOCUMENTS 

tokenized_device = [doc.lower().split( ) for doc in device_docs]


bm25 = BM25Okapi(tokenized_device)

query = "Google".lower().split()
scores = bm25.get_scores(query)


def sparse_search(query):
    query = query.lower().split()
    scores = bm25.get_scores(query)
    sorted_scores = sorted(enumerate(scores),key = lambda x : x[1] , reverse=True)
    # for index , score in sorted_scores:
    #     print(f"Document: {device_docs[index]} , Score: {score}")
    return sorted_scores


print("------------------------------------------------------------------")
print(f"sorted scores: {sparse_search('Google')}")