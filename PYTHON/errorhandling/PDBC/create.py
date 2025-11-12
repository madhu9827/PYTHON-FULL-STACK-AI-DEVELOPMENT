import mysql.connector 
dncon=None
cursor=None
try:
    dbcon=mysql.connector.connect(host='loaclhost',
                                 user='root',
                                 password='root',
                                 database='database1')
    cursor=dbcon.cursor()
    sql_str='''CREATE TABLE employee(
            eid int,
            ename varchar(32)
            );
            '''
    cursor.execute(sql_str)
    print('table created successfully')
except mysql.connector.SQLError as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()