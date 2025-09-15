numbers=[10,20,30,40]
map_obj=map(lambda num:num+1,numbers)
new_numbers=list(map_obj)
print(new_numbers)


print(list(map(lambda x:x+1,[10,20,30,40])))