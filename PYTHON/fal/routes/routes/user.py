from fastapi import APIRouter

router = APIRouter(prefix="/user")
'''
Create User:
------------ 
Usage : Create new User 
URL : http://127.0.0.1:8000/user/create 
Method Type:POST 
Required Fields: uname,email,gender,loc
Access Type:Public
'''
@router.post("/create")
def create_user():
    return {"msg":"New user Created"}

'''
Usage : Fetch all users 
URL : http://127.0.0.1:8000/user/ 
Method Type:GET
Required Fields: None 
Access Type:Public
'''
@router.get("/")
def fetch_all_users():
    return {"msg":"Fetching all users"}

'''
Read One User:
------------ 
Usage : Fetch user by user Id
URL : http://127.0.0.1:8000/user/101
Method Type:GET
Required Fields: None 
Access Type:Public
'''
@router.get("/{uid}")
def get_user(uid:int):
    return {"msg":"Fetching user details",'uid':uid}


'''
Update User:
------------ 
Usage : update user by Id
URL : http://127.0.0.1:8000/user/update/101
Method Type:PUT
Required Fields: uname,email,gender,loc  
Access Type:Public
'''
@router.put("/update/{uid}")
def update_user(uid:int):
    return {"msg":"Updating user by id", 'uid':uid}


'''
Delete User:
------------ 
Usage : update user by Id
URL : http://127.0.0.1:8000/user/delete/101
Method Type:DELETE
Required Fields: uname,email,gender,loc  
Access Type:Public

'''
@router.delete("/delete/{uid}")
def delete_user(uid:int):
    return {"msg":"Deleting user", 'uid':uid}