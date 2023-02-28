from fastapi import FastAPI, Depends, status, Response, HTTPException
from .import schemas, models
from . database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

# created a blog post        
@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog, db: Session = Depends(get_db)):
    new_blog  = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# deleted a blog post
@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with the id {id} not available')
        
    blog.delete(synchronize_session=False)
    db.commit()
    return "Blog deleted successfully"
    

# update the blog with the specified id
@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with the id {id} not available')
    blog.update({models.Blog.title: request.title, models.Blog.body: request.body})
    db.commit()
    return "Blog updated successfully"
    



# view the all blog entries
@app.get("/blog")
def all_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


# view the all blog entries with the specified id
@app.get("/blog/{id}", status_code=200)
def show(id, response:Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with the id {id} not available')
    return blogs
