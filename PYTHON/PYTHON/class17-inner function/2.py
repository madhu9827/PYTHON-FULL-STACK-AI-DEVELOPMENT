def outer():
    print('outer function')
    def inner():
        print('inner function')
    return 10
outer()
# inner()//name error
# how to invoke inner function from outside--return the inner function reference
inn=outer()
print(inn)