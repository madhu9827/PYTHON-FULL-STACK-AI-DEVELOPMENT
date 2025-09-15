def user_module():
    def login():
        print("login success")
    def logout():
        print("logout success")
    return login
x=user_module()
x()
x()