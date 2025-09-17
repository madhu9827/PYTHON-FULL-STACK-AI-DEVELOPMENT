import csv
fp=open('emp.csv','r')
emp_data=csv.reader(fp)
print(emp_data)
print(type(emp_data))
for emp in emp_data:
    print(emp)

for emp in list(emp_data)[1:]:
    print(emp[1])
