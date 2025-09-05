fruits= ["apple", "banana", "cherry", "apple", "mango"]
print(fruits.count("apple"))
index=fruits.index("banana")
fruits[index]="grapes"
print(fruits[index])
fruits.insert(2,"orange")
fruits.pop()
print(fruits)