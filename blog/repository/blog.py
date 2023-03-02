from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def create(request:schemas.Blog, db: Session):
    new_blog  = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    
    
def delete(id:int, db: Session):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with the id {id} not available')
        
    blog.delete(synchronize_session=False)
    db.commit()
    return "Blog deleted successfully"


def update(id:int, request:schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with the id {id} not available')
    blog.update({models.Blog.title: request.title, models.Blog.body: request.body})
    db.commit()
    return "Blog updated successfully"
 
 
def show(id:int, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with the id {id} not available')
    return blogs


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

