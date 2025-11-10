import requests,json

resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
print(type(resp_data)) #<class 'requests.models.Response'>
users=resp_data.json()
# fp=open('data.json','w')
# json.dump(users,fp)
# print("new file is created")
# fp.close()
with open('user.json','w') as file:
    json.dump(users,file)
print("new  file is created")