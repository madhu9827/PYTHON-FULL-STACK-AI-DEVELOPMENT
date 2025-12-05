try:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    print(a/b)
except (TypeError,ValueError,ZeroDivisionError) as err:
    print(err)
print("gm")