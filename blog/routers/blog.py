from fastapi import APIRouter, Depends, status, HTTPException, Response
from ..import schemas, database, models
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(
    
    prefix="/blog" ,
    tags=['Blogs']
   
    )

get_db = database.get_db



@router.get("/", response_model= List[schemas.ShowBlog])
def all_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

# created a blog post        
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog, db: Session = Depends(get_db)):
    new_blog  = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# deleted a blog post
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with the id {id} not available')
        
    blog.delete(synchronize_session=False)
    db.commit()
    return "Blog deleted successfully"
    

# update the blog with the specified id
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with the id {id} not available')
    blog.update({models.Blog.title: request.title, models.Blog.body: request.body})
    db.commit()
    return "Blog updated successfully"
    

# view the all blog entries with the specified id
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, response:Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with the id {id} not available')
    return blogs

