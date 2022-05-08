import pymongo
import pandas as pd

collectionName = 'NKUST_POA_2'

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["article"]
mycol = mydb[collectionName]

def LoadPyMongo():
    list_pymongo = []
    for i in mycol.find():
        list_pymongo.append(i)
    
    df = pd.DataFrame(list_pymongo)
    return df



