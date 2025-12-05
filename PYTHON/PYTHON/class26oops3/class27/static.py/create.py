import requests
import mysql.connector

url='https://dummyjson.com/users'
response=requests.get(url)

sql_users=[]
data=response.json()
users=data['users']
 
for user in users:
    sql_users.append((user['id'],
                      user['lastName'],
                      user['email'],
                      user['gender']
                    ))
db_connector=mysql.connector.connect(host="localhost",
                               user="root",
                               password="root",
                               database='pydb'
                              )
sql_st='''
        CREATE TABLE  IF NOT EXISTS sql_users(
        user_id int,
        user_name varchar(32),
        email varchar(50),
        gender varchar(6)
        );
        '''
sql_st2='''
        insert into sql_users(user_id,user_name,email,gender)
        VALUES(%s,%s,%s,%s)
        '''

cursor=db_connector.cursor()
cursor.execute(sql_st)
cursor.executemany(sql_st2,sql_users)
db_connector.commit()
print("table created successfully")
cursor.close()
db_connector.close()