from pydantic import BaseModel

class ItemIn(BaseModel):
    id: int
    is_offer: bool

class ItemOut(BaseModel):
    name: str
    price: float
    is_offer: bool
