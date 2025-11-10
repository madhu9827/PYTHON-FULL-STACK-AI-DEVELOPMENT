import requests,csv,json
res=requests.get('https://dummyjson.com/products')
products=res.json()['products']
# fp1=open('prod.csv','w')
# fp2=open('prod.json','w')
# prod_csv=[]
# prod_json=[]
beauty=0
# for product in products['products']:
#     prod_csv.append((product['id'],
#                     product['title'],
#                     product['category']))
#     prod_json.append({"pid":product['id'],
#                     "ptitle":product['title'], 
#                     "pcategory":product['category']})
# print(prod_csv)
# print(prod_json)
for product in products:
    if product['category']=="beauty":
        beauty+=1
print("no of beauty:",beauty)


o

