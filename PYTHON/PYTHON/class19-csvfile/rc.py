import csv
fp=open('users.csv','r')
users_data=csv.DictReader(fp)
next(users_data)
Male_users=[]
for user in users_data:
    if user['gender']=='Male':
        Male_users.append(user['uname'])
print("male users",Male_users)