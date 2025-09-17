import csv
fp=open('users.csv','r')
users_data=csv.DictReader(fp)
next(users_data)
Female_users=[]
for user in users_data:
    if user['gender']=='Female':
        Female_users.append(user['uname'])
print("female users",Female_users)