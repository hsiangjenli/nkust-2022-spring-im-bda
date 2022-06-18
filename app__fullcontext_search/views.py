from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import pymongo, json
from bson import json_util, ObjectId

collectionName = 'NKUST_POA_2'
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["article"]
mycol = mydb[collectionName]
mycol.create_index([("Title", "text"), ("Context", "text")])


def home(request):
    return render(request, 'app__fullcontext_search/home.html')


@csrf_exempt
def api_fullcontext_search(request):
    keys = request.POST.get('keys')
    print(keys)
    data = []

    for i in mycol.find(
        {"$text": 
            {"$search": keys}},
            { 'Category':1, 'Title': 1, 'Context': 1, 'news_url': 1, 'img_url': 1}
        ).limit(6):
        
        data.append(json.loads(json_util.dumps(i)))

    return JsonResponse({'data': data}, safe=False)

