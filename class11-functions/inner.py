def user_module():
    def login():
        print("login success")
    def logout():
        pass
    return 100
inner=user_module()
print(type(inner))



def user_module():
    print("login success")
    def login():
        print("login")
    def logout():
        pass
    return login
inn=user_module()
print(type(inn))#<class 'function'>
                    #<function user_module.<locals>.login at 0x000001FD403D1440
print(inn)