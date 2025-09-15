a=lambda a,b:a*b
print(a(2,3))

b=lambda x:x*x*x
print(b(3))

numbers=["madhu","lali","nithi"]
obj=map(lambda x:x.upper(),numbers)
print(list(obj))

numbers=[2,3,4,5,6]
obj=filter(lambda x:x%2==0,numbers)
print(list(obj))

num=[2,3,4,5]
obj=map(lambda x:x+2,num)
print(list(obj))