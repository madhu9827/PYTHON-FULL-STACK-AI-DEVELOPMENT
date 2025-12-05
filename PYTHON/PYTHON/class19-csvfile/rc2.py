import csv
fp=open('users.csv','r')
users_data=csv.DictReader(fp)
next(users_data)
for user in users_data:
    print(user['gender'])