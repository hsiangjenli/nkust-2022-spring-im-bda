import pandas as pd 
import pymongo
import re

collectionName = 'NKUST_POA'

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["article"]
mycol = mydb[collectionName]
pymongoData = []

for i in mycol.find():
    pymongoData.append(i)

df = pd.DataFrame(pymongoData)

# df.to_csv('dataset/fromMonogoDB.csv', index=False)

def IterKeyRiseFall(x):
    rise = len(re.findall(r'上漲', x))
    fall = len(re.findall(r'下跌', x))
    return rise, fall

def CountRiseFall(df, cats):
    outputs = {'Rise':0, 'Fall': 0}
    for cat in cats:
        df_cat = df[df.Category==cat]
        for rise, fall in df_cat.Context.apply(IterKeyRiseFall):
            outputs['Rise'] += rise
            outputs['Fall'] += fall
    return outputs