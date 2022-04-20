from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from collections import Counter


def home(request):

    return render(request, 'app__top_person/home.html')


def NerToken(word, ner, idx):
    return ner, word


@csrf_exempt
def api_post_top_person(request):

    df = pd.read_csv('app__api/dataset/from_Monogo_DB.csv')

    cat = request.POST.get('news_category')
    topk = request.POST.get('topk')
    topk = int(topk)

    allNE = []

    df_cat = df[df.Category == cat] if cat != '全部' else df

    for ne in df_cat.entities:
        allNE += eval(ne)

    filtered_words = []
    for ner, word in allNE:
        if (len(word) >= 2) & (ner in ['PERSON']):
            filtered_words.append(word)

    counter = Counter(filtered_words)
    outputs = counter.most_common(topk)

    keys = []
    values = []
    for key, value in eval(str(outputs)):
        keys.append(key)
        values.append(value)

    response = {'chart_data':  {"category": cat,
                                "labels": keys,
                                "values": values}
                }

    return JsonResponse(response, safe=False)
