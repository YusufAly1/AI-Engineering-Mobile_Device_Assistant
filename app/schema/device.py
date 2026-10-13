from pydantic import BaseModel , Field 
from typing import Literal 


class Device (BaseModel) : 

    brand : str = Field(min_length = 3)
    model : str = Field(min_length = 3)
    specs : dict[str , str] 
    release_year : int 
    price_tier : Literal["budget", "mid-range","flagship"] 



class ExtractRequest(BaseModel) : 
    text : str = Field(min_length=3)


class ExtractResponse (Device) : 
    pass


class SearchRequest (BaseModel) : 
    q:str = Field(min_length=3 , max_length=500)

class SearchResult (BaseModel) : 
    document: str
    score: float
    

class SearchResponse(BaseModel) : 
    results: list[SearchResult]

