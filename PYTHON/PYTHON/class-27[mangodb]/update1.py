import requests
import pymongo
from pymongo import MongoClient
dbcon=MongoClient('mongodb://localhost:27017/')
db=dbcon['dbone']
product_col=db['products']
products=product_col.find()
#read
for product in products:
    print(product['title'])
#update
res1=product_col.update_one({"title":"Red Nail Polish"},
                       {"$set":{"price":400}}
                       )
res2=product_col.update_many({"category":"beauty"},
                        {"$set":{"in_stock":True}}
                        )
print(res1)
print(res2)
res3=product_col.delete_one({"title":"Red Lipstick"})
print(res3)
res4=product_col.delete_many({"category":"beauty"})
print(res4) #delete everything