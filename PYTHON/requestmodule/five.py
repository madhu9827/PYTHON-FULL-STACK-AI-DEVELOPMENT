import requests,json,csv
fp1=open("emp.json",'w')
fp2=open("emp.csv",'w')
res=requests.get('https://jsonplaceholder.typicode.com/users')
users=res.json()
# transform for csv file
user1=[]
for user in users:
    user1.append((user['id'],user['username'],user['email'],user['address']['city']))

cw=csv.writer(fp2)
cw.writerow(["uid","uname","email","city"])
cw.writerows(user1)




