from datetime import date
from pydantic import BaseModel


class create(BaseModel):
    fullname: str
    email: str
    password:str
    dob: str
    contactnumber: int
    gender: str
    selectcourse:str
    reason : str
   

class update(create):
    pass

class view (BaseModel):
    fullname: str
    email: str
    password:str
    dob: date
    contactnumber: int
    gender: str
    selectcourse:str
    reason : str
    
    created_at: date

    class Config:
        orm_mode = True
 

class newPost(BaseModel):
    title:str
    content:str

class response(BaseModel):
    title:str
    content:str
    owner_id:int
    owner:view

    class Config:
        orm_mode = True

class vote(BaseModel):
    post_id : int
    dir : int

    class Config:
        orm_mode =True        