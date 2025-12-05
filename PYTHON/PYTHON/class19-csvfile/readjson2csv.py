import json,csv
fp1=open('users.json','r')
fp2=open('users.csv','w')
users=json.load(fp1)
#print(users)
new_users=[]
for user in users:
    new_users.append((user['u_id'],user['u_name'],user['gender']))
cw=csv.writer(fp2)
cw.writerow(['uid','uname','gender'])
cw.writerows(new_users)
print("New CSV File Created")