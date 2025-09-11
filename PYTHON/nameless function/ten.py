names=['rahul','sonia','priyanka','modi','amith']
map_obj=map(lambda w:w.upper(),names )
print(list(map_obj))  #using with map and lambda function


enames=[]
for name in names:
    enames.append(name.upper())
print(names)
print(enames)  #without map
