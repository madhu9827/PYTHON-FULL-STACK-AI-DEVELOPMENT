# read json file and print data
# read json file and print all employees names
import json
fp=open('data.json','r')
employees=json.load(fp)
for emp in employees:
    print(emp['ename'])

fp.close()