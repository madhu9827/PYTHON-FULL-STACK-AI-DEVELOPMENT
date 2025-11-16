import requests,json,pymongo,csv,_mysql_connector
resp=requests.get("https://dummyjson.com/products")
product_data=resp.json()
products=product_data['products']
print(len(products))
# transform
products_json=[]
products_csv=[]
for prod in products:
    products_json.append({"pid":prod['id'],
                          "name":prod['title'],
                          "price":prod['price'],
                          "category":prod['category'],
                          "rating":prod['rating']
                          })
    products_csv.append((prod['id'],prod['title'],prod['price'],prod['category'],prod['rating']))

# print(products_json)
# load--into json and mongodb-collection
fp2=open("products.json","w")
json.dump(products_json,fp2)
print('file is created successfully')
# load
fp1=open("product_csv","w",newline="")
csv_obj=csv.writer(fp1)
csv_obj.writerow(["id","title","price","category","rating"])
csv_obj.writerows(products_csv)
print("new csv file is created")

try:
    client=pymongo.MongoClient('mongodb://localhost:27017/')
    db=client['db4']
    product_col=db(products_json)
    print()