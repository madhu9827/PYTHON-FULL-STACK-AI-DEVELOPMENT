from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def index_page():
    return{"msg":"index page created"}
# class user(BaseModel):
#     id=id
#     name=str
    
@app.post('/create')
def create_user():
    return{"msg":"user is created"}
@app.get('/read')
def get_user():
    return{"msg":"get user details"}
@app.put('/update')
def update_user():
    return{"msg":"user updated"}
@app.delete('/delete')
def delete_user():
    return{"msg":"user deleted"}