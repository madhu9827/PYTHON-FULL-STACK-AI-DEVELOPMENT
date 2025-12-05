def user_module():
    def login():
        print("login success")
    def logout():
        print("logout success")
    return 100
x=user_module()
print(x)