names=['rahul','sonia','priyanka','modi','amith']
obj=filter(lambda name:name.startswith('r'),names)
print(list(obj)) #with filter and lambda


def change_case(name):
    return name.startswith('r')
new_users=filter(change_case,names)
print(list(new_users))  #with filter function


new_users=[]
for name in names:
    if name.startswith('r'):
        new_users.append(name) 
         #without filter
print(names)
print(new_users)