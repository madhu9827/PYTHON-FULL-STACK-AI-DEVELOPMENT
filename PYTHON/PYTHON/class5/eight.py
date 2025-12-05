fruits = {"apple", "banana", "mango", "orange"}
tropical = {"mango", "pineapple", "papaya"}
union_set=fruits.union(tropical)
print("union:",union_set)
intersect_set=fruits.intersection(tropical)
print("intersect:",intersect_set)
difference_set=fruits.difference(tropical)
print("difference(fruits-tropical):",difference_set)