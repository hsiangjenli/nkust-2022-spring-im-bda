from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import numpy as np
from django.views.decorators.csrf import csrf_exempt
from .prepare import CountRiseFall

keyRiseFall = ['上漲', '下跌']
catTaiwan = ['tw_stock_news', 'tw_macro', 'tw_quo']


@csrf_exempt
def api_twii_5mins(request):

    twii5mins = pd.read_csv('app__api/dataset/twii_5_mins.csv')
    fromMongoDB = pd.read_csv('app__api/dataset/fromMonogoDB.csv')

    color = '#C0AA7A' if twii5mins['TAIEX'][0] > twii5mins['TAIEX'].iloc[-1] else '#D9D9D9'
    outputsRiseFall = CountRiseFall(df=fromMongoDB, cats=catTaiwan)
    twii5minsJson = {
        'Time': twii5mins['Time'].to_list(),
        'Index': twii5mins['TAIEX'].to_list(),
        'Zero': list(np.zeros(len(twii5mins['Time']))),
        'Color': color
    }
    twii5minsJson.update(outputsRiseFall)
    return JsonResponse(twii5minsJson, safe=False)



