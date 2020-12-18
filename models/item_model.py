from pydantic import BaseModel

class ItemIn(BaseModel):
    id: int
    

class ItemOut(BaseModel):
    name: str
    price: float
    is_offer: bool
