s1=set()
print(type(s1))
s2={12,12,34,56,78}
print(s2)
s2.add(40)
print(s2)
s2.update(s1)
print(s2)
print(len(s2))
s3=s2.copy()
print(s3)
s2.pop()
print(s2)
s2.remove(56)
print(s2)
s2.discard(56)
print(s2)
s2.clear()
print(s2)


s1 = {12, 34, 56, 47}
s2 = {12, 45, 56, 78}

print("Union:", s1.union(s2))                 # {34, 47, 12, 45, 78, 56}
print("Difference:", s1.difference(s2))       # {34, 47}
print("Intersection:", s1.intersection(s2))   # {56, 12}
print("Symmetric Difference:", s1.symmetric_difference(s2))  # {34, 45, 47, 78}

print("Original s1 still:", s1)
