import requests
import mysql.connector,json,csv
#extract
response=requests.get('https://dummyjson.com/products')
data=response.json()
products=data['products']
new_products=[]
for product in products:
    new_products.append((product['id'],product['title'],product['category'],product['price']))
print(new_products)
try:
    db_connector=mysql.connector.connect(host="localhost",
                               user="root",
                               password="root",
                               database='etdb'
                              )
    st1 = '''
        CREATE TABLE IF NOT EXISTS new_products (
            product_id INT,
            title VARCHAR(100),
            category VARCHAR(50),
            price DECIMAL(10,2)
        );
        '''
    st2='''
        insert into new_products(product_id,title,category,price)
        VALUES(%s,%s,%s,%s)
        '''
    cursor=db_connector.cursor()
    cursor.execute(st1)
    cursor.executemany(st2,new_products)
    db_connector.commit()
    print("table created successfully")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    db_connector.close()

fp=open('products.csv','w',newline='')
cw=csv.writer(fp)
cw.writerow(['product_id','title','category','price'])
cw.writerows(new_products)
print(new_products)

fp2=open('products.json','w')
json.dump(new_products,fp2)
print("New JSON File Created")