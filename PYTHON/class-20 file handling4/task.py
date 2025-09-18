import requests,json,csv
response=requests.get('https://jsonplaceholder.typicode.com/users')
users=response.json()
print(type(users))

new_users=[]
new_users_csv=[]
for user in users:
    new_users.append({"id":user['id'],
                      'name':user['username'],
                      'city':user['address']['city'] })
    new_users_csv.append((user['id'],
                          user['username'],
                          user['address']['city'],
                          user['phone']))
#print(new_users)
#print(new_users_csv)


fp1=open('users.json','w')
json.dump(new_users,fp1)
print("new json file is created")

fp2=open('users.csv','w',newline='')
cw=csv.writer(fp2)
cw.writerow(['uid','username','city','phoneno'])
cw.writerows(new_users_csv)
print("New CSV File Created")

fp1.close()
fp2.close()