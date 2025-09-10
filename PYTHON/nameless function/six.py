numbers=[11,18,31,7,8,232]
even_num=[]
for num in numbers:
    if num%2==0:
        even_num.append(num)
print(even_num)

numbers=[11,18,31,7,8,232]
filter_obj=filter(even_num,numbers)
print(filter_obj)

numbers=[11,18,31,7,8,232]
filter_obj=filter(lambda num:num%2==0,numbers)
print(list(filter_obj))