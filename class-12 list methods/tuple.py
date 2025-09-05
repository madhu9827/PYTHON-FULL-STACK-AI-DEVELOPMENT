tuple=("blue","red","blue","blue","green")
print(tuple.index("red"))
print(tuple)
print(tuple.count("blue"))
 #tuple.append("pink") #AttributeError: 'tuple' object has no attribute 'append'


my_tuple=(5,7,8,9)
print("original tuple:",my_tuple)
my_list=list(my_tuple)
print("convert list to :",my_list)
my_list.append(4)
my_list.append(5)
print(my_list)