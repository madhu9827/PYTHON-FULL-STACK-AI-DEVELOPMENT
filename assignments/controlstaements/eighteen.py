#Program to print max numbers in given 3 numbers ?
a=int(input("enter number:"))
b=int(input("enter number:"))
c=int(input("enter number:"))
num=[a,b,c]
print(max(num))
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)