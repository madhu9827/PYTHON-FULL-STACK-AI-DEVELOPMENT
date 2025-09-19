def verify(func):
    def inner(name):
        if name=="modi":
            print("modi pm")
        else:
            return func(name)
return inner

def wish(name):
    print("hi",name,"gm")
wish("rahul")
wish("sonia")
wish("modi")