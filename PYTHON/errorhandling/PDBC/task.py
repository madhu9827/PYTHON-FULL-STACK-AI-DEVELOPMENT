import mysql.connector,requests
res=requests.get('https://jsonplaceholder.typicode.com/users')
data=res.json()
dbcon=None
cursor=None
dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='taskdb')
print("database created")

cursor=dbcon.cursor()
sql_str='''CREATE TABLE if not exists user(
        uid int,
        name varchar(32),
        email varchar(32),
        city varchar(32)
        );
    '''
cursor.execute(sql_str)
sql_sts2 =''' INSERT INTO user(uid, name, email, city) VALUES (%s, %s, %s, %s)'''
for user in data:
    user_id=user['id']
    user_name=user['name']
    user_email=user['email']
    user_city=user['address']['city']
# values = (sql)
    cursor.execute(sql_sts2,(user_id, user_name, user_email, user_city))
dbcon.commit()
print("All records inserted successfully!")



