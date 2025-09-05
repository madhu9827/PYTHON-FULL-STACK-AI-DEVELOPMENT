class_subjects={
    "John" : {"Math", "Science"},
    "Alice" : {"English", "Science"},
     "Bob" : {"Math", "History"}
}
print(class_subjects['Alice'])#Print all subjects studied by "Alice".
class_subjects["Bob"]  #'Art'#Add "Art" to Bob’s subjects
print(class_subjects)  
common_subjects = class_subjects["John"].intersection(class_subjects["Alice"])
print("Common subjects between John and Alice:", common_subjects)                        #Find common subjects between "John" and "Alice".
unique_subjects = set().union(*class_subjects.values())
print("All unique subjects in the class:", unique_subjects)