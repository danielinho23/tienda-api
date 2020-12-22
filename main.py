from fastapi import FastAPI
from pydantic import BaseModel
from models.item_model import ItemIn, ItemOut
from db.item_db import Item
from db.item_db import get_item, update_item
from db.user_db import get_user, update_user
from db.user_db import UserInDB
from models.user_models import UserIn, UserOut


from fastapi import HTTPException

'''conexion desde front to back end'''
from fastapi.middleware.cors import CORSMiddleware
'''va hasta acá'''

api = FastAPI()

'''conexion desde front to back end'''
origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080", "http://localhost:8000",
    
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)
'''va hasta acá'''

@api.post("/usuario/autentication/")
async def auten_usu(usuario_in: UserIn):
    usuario = get_user(usuario_in.username)
    if usuario == None:
        raise HTTPException (status_code=404, 
                             detail="Usuario no registrado")
    elif usuario.password != usuario_in.password:
        return{"Autenticado":False}
    else:
        return {"Autenticado":True}


@api.post("/producto/{item_id}")
async def item_get(item_id:int):
    item_in = get_item(item_id)
    if item_in == None:
        raise HTTPException(status_code=404,
                detail="El item no fue encontrado")
    item_out = ItemOut(**item_in.dict())
    return item_out


@api.put("/producto/descuento/")
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

               

