
mul=lambda a,b:a*b
print(mul(10,20))
print(type(mul))


x=3
a=lambda x:x%2==0
print(a(x))


num=[10, 15, 20, 25, 30]
obj=filter(lambda x:x%10==0,num)
print(list(obj))

words=['apple', 'kiwi', 'banana', 'fig']
obj=filter(lambda w:len(w)>4 ,words)
print(list(obj))

num=[1, 2, 3, 4, 5]
obj=map(lambda x:x*x*x,num)
print(list(obj))

words=['python', 'java', 'c']
map_obj=map(lambda w:w.upper(),words)
print(list(map_obj))