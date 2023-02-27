from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index():
    return {'data':{"Name": "Aditya Upadhyay"}}

@app.get("/index")
def index(limit):
    # for published blog with limit
    return {'data':f'{limit} blog from the blog database' }

@app.get("/about")
def index(limit, published:bool):
    # for published blog with limit and true, false condition
    if published:
        return {'data':f'{limit} published blog from the blog database' }
    else:
        return {'data':f'{limit} blog from the blog database' }

@app.get("/about/blog")
def index(limit = 10, published:bool = True, sort:Optional[str] = None):
    # for published blog with limit = 10 and true, false condition and sorting
    if published:
        return {'data':f'{limit} published blog from the blog database' }
    else:
        return {'data':f'{limit} blog from the blog database' }


@app.get("/blog/unpublished")
def unpublished():
    return {'data':{"about": "My Unpublished Blogs"}}

@app.get("/blog/{blog_id}")
def show(blog_id:int):
    #fetch the blog with blog_id = blog_id
    return {'data':blog_id}


@app.get("/blog/{id}/comments")
def comments(id):
    #fetch the comments with id = id
    return {'data':{'1','2','3','4','5','6','7','8','9'}}


@app.get("/comments/{id}")
def comments(id, limit=5):
    #fetch the comments with id = id
    return {'data':{'1','2','3','4','5','6','7','8','9'}}

class Student(BaseModel):
    
    name: str
    student_id: int
    subject: str

@app.post("/student") 
def create_student(student:Student):
    return {'data':f"Student name is {student.name}"}
