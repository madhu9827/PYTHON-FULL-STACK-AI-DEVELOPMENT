import requests,json,csv
fp1=open("emp.json",'w')
fp2=open("emp.csv",'w')
res=requests.get('https://jsonplaceholder.typicode.com/users')
users=res.json()
# transform for csv file and jon file
user_csv=[]
user_json=[]
for user in users:
    user_csv.append((user['id'],user['username'],user['email'],user['address']['city']))
    user_json.append({"uid":user["id"],"uname":user["username"],"email":user["email"],"city":user["address"]["city"]})
# load into json file
json.dump(user_json,fp1)
print("json file created")


cw=csv.writer(fp2)
cw.writerow(["uid","uname","email","city"])
cw.writerows(user_csv)
print("csv file is created")

fp1.close()
fp2.close()
