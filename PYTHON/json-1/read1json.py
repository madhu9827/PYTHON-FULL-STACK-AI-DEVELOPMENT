import json
fp=open('data.json','r')
employees=json.load(fp)
# print(employees)
for emp in employees:
    if emp['avail'] == True:
        print(emp['eid'])

fp.close()
        