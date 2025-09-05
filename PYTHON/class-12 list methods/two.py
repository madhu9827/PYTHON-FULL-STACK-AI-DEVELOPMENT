numbers=[1,2,3,4,25]
numbers.pop()
print(numbers)
numbers.remove(3)
print(numbers)
numbers.clear()
print(numbers)


del numbers
print(numbers)  #NameError: name 'numbers' is not defined. Did you forget to import 'numbers'?
