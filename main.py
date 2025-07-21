from fastapi import FastAPI, Depends, Response, HTTPException
import schemas, models
from database import engine
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

@app.post('/blog', status_code=201)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blogs')
def get_all_blogs(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blogs/{id}')
def get_blog(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog
    

@app.delete('/blogs/{id}', status_code=204)
def delete_blog(id:int, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    db.delete(blog)
    db.commit()
    return Response(status_code=204)


@app.put('/blog/{id}', status_code = 202)
def update_blog(id:int, request:schemas.Blog, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f'messageblog with {id} is not found')
    blog.update({'title':'I am updated'})
    db.commit()
    return "Updated Successfully"



@app.get("/blog", status_code=200, response_model=List[schemas.ShowBlog])
def show_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


crypt_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.post('/users')
def create_user(request:schemas.Users, db: Session = Depends(get_db)):
    hashed_password = crypt_cxt.hash(request.password)
    user = models.Users(name = request.name, email = request.email, password = hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user





