s1=set()
s2={10,20,10,20}
print(s2)
s3=s2.copy()
print(s3)
s2.add(30)
print(s2)
s2.update(s3)
print(s3)
s1.union(s2)
s1.intersection(s2)
print(s2)
s1.difference(s3)
print(s3)
s2.remove(20) #remove specified element for set object
print(s2) #{10, 30}
s2.remove(30)
print(s2) #KeyError: 50
s2.discard(50)
s2.pop()
print(s2)