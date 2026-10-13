from fastapi import FastAPI 
from app.services.extraction import extract_device 
from app.schema.device import SearchRequest , SearchResult ,SearchResponse
from app.services.search import hybrid_search
app = FastAPI()

@app.post("/extract") 

def extract (text : str): 
    return extract_device(text)


@app.post("/search" , response_model=SearchResponse) 
def search (request : SearchRequest  ) : 
    results  = hybrid_search(request.q)
    return {"results" : results}
    
  
