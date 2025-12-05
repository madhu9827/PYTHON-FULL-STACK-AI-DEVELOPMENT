import json
fp=open('emp.json','r')
employees=json.load(fp)
print(type(employees))

for emp in employees:
    if emp['avail']== True:
        print(emp['ename'])



for emp in employees:
    if emp['avail']== False:
        print(emp['ename'])
