a=int(input("enter number:"))
b=int(input("enter number:"))
c=int(input("enter number:"))
num=[a,b,c]
print(min(num))
min_num = a if a < b else b
min_num = min_num if min_num < c else c