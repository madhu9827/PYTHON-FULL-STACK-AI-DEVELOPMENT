import json,csv
fp1=open('users.json','r')
fp2=open('males.csv','w',newline='')
users=json.load(fp1)
#print(users)
male_users=[]
for user in users:
    if user['gender']=='Male':
        male_users.append((user['u_id'],user['u_name'],user['gender']))
cw=csv.writer(fp2)
cw.writerow(['uid','uname','gender'])
cw.writerows(male_users)
print("New CSV File Created")