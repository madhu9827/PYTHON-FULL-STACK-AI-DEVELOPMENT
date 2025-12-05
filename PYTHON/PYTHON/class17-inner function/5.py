def outer():
    print("outer function")
    def f1():
        print("f1")
    def f2():
        print("f2")
    return f1,f2
inn=outer()
print(inn)
inn[0]()
inn[1]()