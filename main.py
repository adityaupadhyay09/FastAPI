from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {'data':{"Name": "Aditya Upadhyay"}}

@app.get("/index")
def index(limit):
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


