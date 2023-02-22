from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.post("/blog")

class Blog(BaseModel):
    title:str
    blog:str
    
def create_blog(request:Blog):
    return request

# def create(title, blog):
#     return {'title': title, 'blog': blog}