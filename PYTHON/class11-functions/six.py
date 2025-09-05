def outer():
    print("outer function started")
    def inner():
        print("inner function")
    inner()
    inner()
outer()
inner()  #NameError: name 'inner' is not defined. Did you mean: 'iter'?