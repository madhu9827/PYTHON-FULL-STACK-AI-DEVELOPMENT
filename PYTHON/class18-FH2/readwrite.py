#read a
import json
fp1=open('users.json','r')
fp2=open('employees.json','w')
users=json.load(fp1)
print(type(users))
print(len(users))
#write users data into new file ie employees.json
json.dump(users,fp2)
print("new file json created")
fp1.close()
fp2.close()
