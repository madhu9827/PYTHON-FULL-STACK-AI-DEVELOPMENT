def login_req(func):
    def inner(is_login):
        if is_login==False:
            print("login requested")
        else:
            return func(is_login)
    return inner