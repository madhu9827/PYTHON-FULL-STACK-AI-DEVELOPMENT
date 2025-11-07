import json
fp=open('data1.json','r')
employees=json.load(fp)
print("no of employees",len(employees))
count=0
counts=0
for emp in employees:
    if emp['gender']=="Female":
        count+=1
    if emp['gender']=="Male":
        counts+=1
print("no of female employees",count)
print("no of male employees ",counts)

fp.close()