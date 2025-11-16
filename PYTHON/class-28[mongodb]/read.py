import pymongo
from pymongo import MongoClient
try:
    client=MongoClient("mongodb://localhost:27017/")
    db=client['db4']
    user_col=