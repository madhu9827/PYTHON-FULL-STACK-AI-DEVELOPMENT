#9.Print max numbers in given 3 numbers- using Ternary Operator?
a=int(input("enter number:"))
b=int(input("enter number:"))
c=int(input("enter number:"))
num=[a,b,c]
print(max(num))
max_num=a if a > b else b
max_num=max_num if max_num > c else c