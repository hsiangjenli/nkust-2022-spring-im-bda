from django.shortcuts import render
from django.http import  JsonResponse, HttpResponse
import pandas as pd
import numpy as np
from django.views.decorators.csrf import csrf_exempt
from .prepare import CountRiseFall
from .helper import LoadPyMongo

keyRiseFall = ['上漲', '下跌']
catTaiwan = ['tw_stock_news', 'tw_macro', 'tw_quo']
global df
df = LoadPyMongo().sort_values(by='Date')

@csrf_exempt
def api_twii_5mins(request):

    twii5mins = pd.read_csv('app__api/dataset/5twii.csv')
    
    color = '#C0AA7A' if twii5mins['TAIEX'].iloc[-1] > twii5mins['TAIEX'][0] else '#D3D3D3'
    fillcolor = 'rgba(192, 170, 122, 0.2)' if twii5mins['TAIEX'].iloc[-1] > twii5mins['TAIEX'][0] else 'rgba(211, 211, 211, 0.2)'

    outputsRiseFall = CountRiseFall(df=df, cats=catTaiwan)
    time = twii5mins['Time'].to_list()

    json = []
    for t, twii in zip(twii5mins['Time'], twii5mins['TAIEX']):
        row = {'x': str(t), 'y': twii}
        json.append(row)

    twii5minsJson = {
        'Time': time,
        'Index': twii5mins['TAIEX'].to_list(),
        'Color': color,
        'FColor': fillcolor,
        'Json': json,
    }
    twii5minsJson.update(outputsRiseFall)
    return JsonResponse(twii5minsJson, safe=False)

def api_twii(request):
    with open('app__api/dataset/twii.csv', encoding = 'utf-8') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=app__home_page/dataset/twii.csv'
        return response

