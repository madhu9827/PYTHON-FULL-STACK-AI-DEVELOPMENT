import mysql.connector
dbcon=mysql.connector.connect(host="localhost",
                              user='root',
                              password='root',
                              database='onedb')
cursor=dbcon.cursor()
cursor.execute("select * from employee")
employee=cursor.fetchall()
print(type(employee))
for emp in employee:
    print(emp)

print("done")