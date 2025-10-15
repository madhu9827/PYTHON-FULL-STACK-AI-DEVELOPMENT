from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Application Root Request"}

@app.get("/about")
def about_page():
    return {"message": "About Page"}

users = [
    {'uid': 101, 'uname': 'Rahul', 'gender': "Male"},
    {'uid': 102, 'uname': 'Sonia', 'gender': "Female"},
    {'uid': 103, 'uname': 'Priyanka', 'gender': "Female"},
    {'uid': 104, 'uname': 'Modi', 'gender': "Male"}
]

@app.get("/users")
def get_users():
    return {"msg": "All user details", "users": users}

@app.get("/users/{uid}")
def get_user(uid: int):
    print(type(uid))
    for user in users:
        if user['uid'] == uid:
            return {"msg": "User found", "user": user}
    return {"msg": "User not found"}
