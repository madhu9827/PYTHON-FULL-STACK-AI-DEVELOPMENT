import requests
import mysql.connector,json,csv
#extract
response=requests.get('https://dummyjson.com/users')
data=response.json()
users=data['users']
#transform
new_users=[]
for user in users:
    new_users.append((user['id'],user['username'],user['email'],user['gender']))
try:
    db_connector=mysql.connector.connect(host="localhost",
                               user="root",
                               password="root",
                               database='pydb'
                              )

    sql_st='''
        CREATE TABLE  IF NOT EXISTS new_users(
        user_id int,
        user_name varchar(32),
        email varchar(50),
        gender varchar(6)
        );
        '''
    cursor=db_connector.cursor()
    sql_st2='''
        insert into new_users(user_id,user_name,email,gender)
        VALUES(%s,%s,%s,%s)
        '''
    cursor.execute(sql_st)
    cursor.executemany(sql_st2,new_users)
    db_connector.commit()
    print("table created successfully")
except mysql.connector.Error as err:
    print(err)
# cursor.execute("select * from employee")
# employee=cursor.fetchall()
finally:
    cursor.close()
    db_connector.close()


fp=open('users.csv','w',newline='')
cw=csv.writer(fp)
cw.writerow(['user_id','name','email','gender'])
cw.writerows(new_users)
print(new_users)

fp2=open('users.json','w')
json.dump(new_users,fp2)
print("New JSON File Created")