from fastapi import APIRouter, Depends, status,Response
from ..import schemas, database, ouath2, models
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog


router = APIRouter(
    
    prefix="/blog" ,
    tags=['Blogs']
   
    )

get_db = database.get_db


# created a blog post        
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog, db: Session = Depends(get_db), current_user: schemas.Admin = Depends(ouath2.get_current_user)):
    return blog.create(request, db)


# deleted a blog post
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db), current_user: schemas.Admin = Depends(ouath2.get_current_user)):
    return blog.delete(id, db)
    

# update the blog with the specified id
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.Admin = Depends(ouath2.get_current_user)):
    return blog.update(id, request, db)
    

# view the blog entries with the specified id
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id:int, response:Response, db: Session = Depends(get_db), current_user: schemas.Admin = Depends(ouath2.get_current_user)):
    return blog.show(id, response, db)


# view all the blog entries with the specified id
@router.get("/", response_model= List[schemas.ShowBlog])
def get_all_blog(db: Session = Depends(get_db), current_user: schemas.Admin = Depends(ouath2.get_current_user)):
    return blog.get_all(db)

