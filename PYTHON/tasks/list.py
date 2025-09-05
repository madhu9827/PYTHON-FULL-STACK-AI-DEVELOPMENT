i=["apple","banana","grapes","kiwi","orange"]
print(i[0])
print(i[-1])
i[1]="mango"
print(i[1])
print(i.append("green grapes"))
i.remove("apple")
print(i)
print("\n i in the list:")
for fruit in i:
    print(fruit)
list1=[2,3,4,5]
list2=[34,56]
result=list1+list2
result.sort()