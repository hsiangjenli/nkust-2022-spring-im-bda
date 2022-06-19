import pymongo
import pandas as pd
from collections import Counter

def LoadPyMongo():
    collectionName = 'NKUST_POA_Job104'

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["article"]
    mycol = mydb[collectionName]

    list_FromMongoDB = []

    for job104 in mycol.find({}, {
        'County': 1,
        'Company': 1,
        'Filtered_JobDescription': 1,
        'Filtered_Others': 1,
        '_id': 0
    }):
        list_FromMongoDB.append(job104)
    df_FromMongoDB = pd.DataFrame(list_FromMongoDB)
    return df_FromMongoDB

def DataFrameToTransaction(df_FromMongoDB):
    list_Transaction = []

    for job104 in df_FromMongoDB.values:
        list_row = []
        for col in job104[[0, 2, 3]]:
            try:
                list_row.extend(col)
            except:
                pass
        if job104[1]:
            list_row.extend([job104[1]])

        list_Transaction.append(list_row)
    return list_Transaction

def ExtractRule(APRIORI_RULE):
    list_From = []
    list_To = []

    for product in APRIORI_RULE:
        try:
            FROM = eval(str(product[2][0][1]))
            TO = eval(str(product[2][0][0]))

            list_From.append(FROM)
            list_To.append(TO)

        except:
            pass
    
    return list_From, list_To

def frozenset(x):
    return ''.join(x)

def ToJsResponse(list_From, list_To):
    list_Nodes = []
    list_Nodes.extend(list_From)
    list_Nodes.extend(list_To)

    counter_list_Nodes = Counter(list_Nodes)

    dict_Nodes = {}
    for i, key in enumerate(counter_list_Nodes):
        dict_Nodes[key] = [i+1, counter_list_Nodes[key]]
    
    list_JS_Nodes = [] # { id: 1, value: 2, label: "Algie" }
    for key, data in dict_Nodes.items():
        color = '#C0AA7A' if key in list_From else '#F2F2F2'
        list_JS_Nodes.append(
            {'id': data[0], 'label': f'<b>{key}</b>', 'color': color, 'value': data[1], 'font': {'multi': "html", 'face': "Noto Sans TC" }}
        )
    
    list_JS_Edges = []
    for f, t in zip(list_From, list_To):
        list_JS_Edges.append(
            {'from': dict_Nodes[f][0], 'to': dict_Nodes[t][0], 'value': 1}
        )
    
    return list_JS_Nodes, list_JS_Edges