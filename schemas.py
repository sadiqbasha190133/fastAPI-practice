from pydantic import BaseModel

class Blog(BaseModel):
    id: int
    title: str
    body: str 

class Users(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(Users):
    name:str
    email:str

    class Config():
        orm_mode = True


class ShowBlog(Blog):
    title:str
    body:str
    creator:ShowUser

    class Config():
        orm_mode = True