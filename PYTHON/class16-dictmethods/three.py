emp={
    'eid':101,
    'ename':'rahul',
    'esal': 45000
}
print(emp.values())
print(type(emp.values()))
 
for value in emp.values():
    print(value)

for key in emp.keys():
    print(key)

for key,value in emp.items():
    print(key,value)