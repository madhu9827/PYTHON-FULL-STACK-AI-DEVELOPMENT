import pymongo
from pymongo import MongoClient
try:
    client=MongoClient('')
    db=client['db']
    user_col=db['users']
    user_col.insert_one({"uid:101,"uname":"rahul"})
    print("Document inserted successfully")
except:
    print("unable to insert")
finally:    
    pass