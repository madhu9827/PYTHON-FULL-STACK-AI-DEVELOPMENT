import csv,json
with open('user.csv','r') as fp:
    csv_reader=csv.reader(fp)
    users=list(csv_reader)
li = []
for user in users[1:]:
    li.append(dict(zip(users[0],user)))
# for i in li:
#     print(i)
with open('one.json','w') as fp:
    json.dump(li,fp)
# with open('one.json','r') as fp1:
#     print(*fp1)



# import pandas as pd

# data = pd.read_csv('user.csv')
# js = [
#     {"use":1,"name":"me"},
#     {"use":1,"name":"me"},
#     {"use":1,"name":"me"}
# ]
# print(data.head())
# print(js)
# print(pd.DataFrame(js))