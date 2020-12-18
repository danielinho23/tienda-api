from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str
    balance: int

database_users = Dict[str, UserInDB]

database_users={
    "Daniel":UserInDB(**{"username":"Daniel",
                        "password":"mintic1",
                        "balance":15000}),
    "Camilo":UserInDB(**{"username":"Camilo",
                        "password":"mintic2",
                        "balance":10000}),
    "Martha":UserInDB(**{"username":"Martha",
                        "password":"mintic3",
                        "balance":20000}),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db