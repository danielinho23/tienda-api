from fastapi import FastAPI
from pydantic import BaseModel
from models.item_model import ItemIn, ItemOut
from db.item_db import Item
from db.item_db import get_item, update_item
from fastapi import HTTPException


api = FastAPI()

@api.get("/producto/{item_id}")
async def item_get(item_id:int):
    item_in = get_item(item_id)
    if item_in == None:
        raise HTTPException(status_code=404,
                detail="El item no fue encontrado")
    item_out = ItemOut(**item_in.dict())
    return item_out

@api.put("/producto/")
async def item_update(item:ItemIn):
    item_in = get_item(item.id)
    if item_in == None:
        raise HTTPException (status_code=404,
                detail="El item no existe")
    if item.is_offer == True:
        item_in.price = item_in.price*0.9
        item_in.is_offer = True
    update_item(item_in)
    item_out= ItemOut(**item_in.dict())
    return item_out

               

