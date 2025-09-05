student={
    'name':'john',
    'age':20,
    'grade':'A'
}
print(student['name'])
student['grade']='B'
print(student)
student['city']="newyork" #add
print(student)
student.pop('age') #remove key
print(student)
for key,value in student.items(): #Loop through the dictionary and print each key → value
    print(f"{key}:{value}")