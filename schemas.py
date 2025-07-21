from pydantic import BaseModel

class Blog(BaseModel):
    id: int
    title: str
    body: str 

class ShowBlog(Blog):
    title:str
    
    class Config():
        orm = True

class Users(BaseModel):
    name:str
    email:str
    password:str