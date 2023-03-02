from fastapi import APIRouter, Depends
from ..import schemas, database
from sqlalchemy.orm import Session
from ..repository import user


router = APIRouter(
    prefix="/user" ,
    tags=['User']
    )

get_db = database.get_db


# create a new user
@router.post("/", response_model=schemas.ShowUser)
def create_user(request:schemas.Admin, db: Session = Depends(get_db)):
    return user.create(request, db)



# get all the user details
@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return user.show(id, db)

