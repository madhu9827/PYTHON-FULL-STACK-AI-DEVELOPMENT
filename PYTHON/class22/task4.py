try:
    num=int(input("enter the integer number:"))
    print("you entered",num)
except ValueError:
    print("it is not a integer")
finally:
    print("conversion finished")