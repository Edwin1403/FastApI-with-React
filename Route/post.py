from fastapi import APIRouter , Depends 
from database import get_db
from sqlalchemy.orm import Session
from auth import current_user
import model , schema
from typing import List

route = APIRouter(
    tags=['Post']
)


@route.post("/newPost",response_model=schema.response )
def Newpost( data:schema.newPost ,db : Session = Depends(get_db) , current_user = Depends(current_user)):
    add = model.Post(**data.dict() , owner_id = current_user)
    db.add(add)
    db.commit()
    db.refresh(add)
    return add
