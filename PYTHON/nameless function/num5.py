fruits = ["apple", "kiwi", "grapes", "fig", "banana"]
small_fruits = []   # new list to store short names
for fruit in fruits:
    if len(fruit) <= 4:   # check each fruit's length
        small_fruits.append(fruit)
print(small_fruits)