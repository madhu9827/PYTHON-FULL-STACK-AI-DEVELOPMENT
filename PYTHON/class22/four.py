try:
    a=int(input("First number"))
    b=int(input("second number"))
    print(a/b)
except ValueError as ve:
    print(ve)
except ZeroDivisionError as err:
    print(err)
print("GM")