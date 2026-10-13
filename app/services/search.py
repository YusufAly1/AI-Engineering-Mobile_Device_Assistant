from app.data.devices import DEVICE_DOCUMENTS 
from app.utils.bm25_index import sparse_search 
from app.utils.embeddings import dense_search



def hybrid_search(query : str , k : int = 3 ) : 

    bm25_sparse = sparse_search(query) 
    embed_dense = dense_search(query)

    score_sparse = {}
    score_dense = {}
    rrf_k = 60 

    rrf_scores = {}


    for rank , (sparse_index_of_doc , score) in enumerate(bm25_sparse , start=1) : 

        score_sparse[sparse_index_of_doc] = (1 / (rrf_k + rank))





    for rank , dense_index_of_doc  in enumerate(embed_dense , start=1 ) : 
        
        score_dense[dense_index_of_doc] =  (1 / (rrf_k + rank))





    for doc_index in score_sparse :
        
        if doc_index in score_dense : 
            rrf_scores[doc_index] = score_sparse[doc_index] + score_dense[doc_index] 

        else : 
            rrf_scores[doc_index] = score_sparse[doc_index]




    for doc_index in score_dense : 
        if doc_index not in score_sparse : 
            rrf_scores[doc_index] = score_dense[doc_index]



    print (f"rrf _ scores before sorting {rrf_scores}")
    ranked_docs = sorted(
        rrf_scores.items(),
        key= lambda item: item[1],
        reverse=True
    )


    # print(f"score_sparse ---: {score_sparse} ")
    # print(f"score_dense ---: {score_dense} ")
    # print(f"rrf scores _________: {rrf_scores}")

    results = []

    for index , score in ranked_docs[:k] : 
        results.append({"document" : DEVICE_DOCUMENTS[index] , "score" :float(score) })

    
    return  results
 



results = hybrid_search("iphone best 8 ram")
for i , k in results :
    print ({k,i})



