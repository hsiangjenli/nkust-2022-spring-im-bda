from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pymongo
import pandas as pd
from .processing import *


df = LoadData()#pd.read_csv('app__api/dataset/from_Monogo_DB.csv')


def home(request):

    return render(request, 'app__user_key/home.html')


@csrf_exempt
def api_get_top_userkey(request):

    userkey = request.POST.get('userkey')
    cate = request.POST.get('cate')
    cond = request.POST.get('cond')
    weeks = int(request.POST.get('weeks'))
    key = userkey.split()

    df_query = filter_dataFrame_fullText(df, key, cond, cate, weeks)
    
    key_freq_cat, key_occurrence_cat = count_keyword(df_query, key)
    
    key_time_freq = get_keyword_time_based_freq(df_query)
    response = {
        'key_occurrence_cat': key_occurrence_cat,
        'key_freq_cat': key_freq_cat,
        'key_time_freq': key_time_freq, }

    # response2 = {'key_occurrence_cat': {'tw_stock_news': 59,
    #                                    'tw_macro': 9,
    #                                    'tw_quo': 2,
    #                                    'wd_macro': 20,
    #                                    'us_stock': 15,
    #                                    'eu_asia_stock': 7,
    #                                    'cn_macro': 1,
    #                                    'hk_stock': 1,
    #                                    'sh_stock': 1,
    #                                    '全部': 115},
    #             'key_freq_cat': {'tw_stock_news': 143,
    #                              'tw_macro': 15,
    #                              'tw_quo': 2,
    #                              'wd_macro': 54,
    #                              'us_stock': 28,
    #                              'eu_asia_stock': 23,
    #                              'cn_macro': 1,
    #                              'hk_stock': 1,
    #                              'sh_stock': 2,
    #                              '全部': 269},
    #             'key_time_freq': [{'x': '2022-04-05', 'y': 12},
    #                               {'x': '2022-04-06', 'y': 32},
    #                               {'x': '2022-04-07', 'y': 39},
    #                               {'x': '2022-04-08', 'y': 25},
    #                               {'x': '2022-04-09', 'y': 7}]}

    return JsonResponse(response, safe=False)
