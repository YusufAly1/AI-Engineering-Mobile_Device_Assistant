
from sentence_transformers import SentenceTransformer
from app.data.devices import DEVICE_DOCUMENTS


device = DEVICE_DOCUMENTS
embed_model = SentenceTransformer("BAAI/bge-small-en-v1.5")

embedding_text = embed_model.encode(device , normalize_embeddings=True)

    
def dense_search(query:str) : 

    query_embed = embed_model.encode(query , normalize_embeddings=True) 
    cosine_similarity =  embedding_text @ query_embed 

    # high_similarity_index = cosine_similarity.argmax()
    # highist_score = cosine_similarity[high_similarity_index]
    # doc_high_score = device[high_similarity_index]
    # print (doc_high_score , float(highist_score))

    ranked_indices = cosine_similarity.argsort()[::-1]

    return ranked_indices
    



result = dense_search("iphone") 
for rank , doc_index  in enumerate(result , start = 1) : 
    print(f"index of document : {doc_index} ---> rank of document :  {rank}" )






