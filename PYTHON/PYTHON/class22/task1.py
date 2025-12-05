try:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a/b)
except ValueError as ve:
    print(ve)
except ZeroDivisionError  as err:
    print("cannot divide by 0")    
finally:
    print("division operator is finished")  