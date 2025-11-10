import csv
fp=open('emp.csv','w',newline='')
cw=csv.writer(fp)
cw.writerow(["eid","ename","esal"])
data=[(101,"rg",45000),
      (102,"sg",35000),
      (103,"pg",45000)
    ]
cw.writerows(data)
print("new file created")
fp.close()
