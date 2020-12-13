from typing import Dict
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    price: float
    is_offer: bool

database_items = Dict[int, Item]
database_items = {100:Item(**{"id":100,
                              "name": "Galletas",
                              "price": 350.6,
                              "is_offer": False  }),
                  101:Item(**{"id":101,
                              "name": "Pan",
                              "price": 250,
                              "is_offer": False  }),  
                              }

def get_item(llave: int):
    if llave in database_items.keys():
        return database_items[llave]
    else:
        return None

def update_item(item: Item):
    database_items[item.id] = item
    return item