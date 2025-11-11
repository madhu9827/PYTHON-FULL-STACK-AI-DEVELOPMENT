try:            
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    print(a/b)
except ValueError as err:
    print("enter integer only")
except ZeroDivisionError as err:
    print("canot divide zero")
print("GE")