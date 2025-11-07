#  read json file write employees data into new json file 
import json
fp=open('data.json','r')
fp1=open('emp.json','w')
employees=json.load(fp)
print(employees)
json.dump(employees,fp1)
print("new json file created successfully")
fp.close()
fp1.close()