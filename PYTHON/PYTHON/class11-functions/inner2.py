def user_module(name,status):
    print("user module function started")
    def login():
        print("login success")
    def logout():
        print("logout success")
    if status==True:
        return login
    else:
        return logout
inner=user_module("RG",True)
inner()