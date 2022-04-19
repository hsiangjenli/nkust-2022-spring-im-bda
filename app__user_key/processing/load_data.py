import pymongo
import pandas as pd

collectionName = 'NKUST_POA'
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["article"]
mycol = mydb[collectionName]

def LoadData():
    pymongoData = []

    for i in mycol.find():
        pymongoData.append(i)

    df = pd.DataFrame(pymongoData)
    return df