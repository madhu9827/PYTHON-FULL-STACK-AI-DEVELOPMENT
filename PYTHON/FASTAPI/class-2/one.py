from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
@app.get('/')
def index_page():
    return{"msg":"index page"}
users=[]
class User(BaseModel):
    id:int
    name:str
    loc:str
@app.post('/create')
def create_user(user:User):
    print(user)
    users.append(user)
    return{"msg":"user created success"}
@app.get('/read')
def get_users():
    return{"users":users}
