#read emp.json file and print emp values
import json
fp=open('emp.json','r')
employees=json.load(fp)
print(employees)
print(type(employees))
for emp in employees:
    print(emp['ename'])