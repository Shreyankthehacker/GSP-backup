from pydantic import BaseModel,Field
from typing import List

class User(BaseModel):
    name : str 
    logo : str 
    description : str
    services: List[str] 