import mysql.connector
dbcon=None 
cursor=None
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='database1')
    print(dbcon.is_connected())
    cursor=dbcon.cursor()
    sql_st='''insert into employee values(101,"Rahul"),
              (102,"madhu"),
              (103,"nithi");     
             '''
    cursor.execute(sql_st)
    dbcon.commit()
    print("Data Inserted Successfully")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()