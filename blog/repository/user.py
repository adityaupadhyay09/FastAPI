from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from ..hashing import Hash


def create(request: schemas.Admin, db:Session):
    new_user = models.Admin(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id:int, db:Session):
    user = db.query(models.Admin).filter(models.Admin.id == id).first()
    
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'User with the id {id} not available')
        
    return user

