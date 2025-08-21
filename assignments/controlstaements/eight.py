#Program to check if a number is a 3-digit number or not?
num=int(input("enter  a digit:"))
if num in range(100,999):
    print("enter number is 3 digit number")
else:
    print("enter number is not a 3 digit number")