from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import  JsonResponse, HttpResponse
import json
import numpy as np
import pandas as pd
from operator import itemgetter
import app__api.views as api
global df
df = api.df

news_sim_martrix = np.load('app__overview/dataset/news_sim_martrix.npy')

item_id2idx={}
for id, i in df.newsId.items():
    item_id2idx[i] = id

def home(request):
    return render(request, 'app__overview/home.html')

@csrf_exempt
def api__latest_new_and_similar_news(request):
    r = api_query_keyword_cate_news()
    return JsonResponse(dict(r))

def api_query_keyword_cate_news():
    cate = 'tw_stock_news'
    user_keywords = ['台股', '台灣']
    cond='or'
    response = get_userkeyword_cate_latest_news(cate, cond, user_keywords)
    return {"latest_news": response}

def get_userkeyword_cate_latest_news(cate, cond, user_keywords):
    
    condition = (df.Category == cate) 
    
    if (cond == 'and'):   
        condition = condition & df.Context.apply(lambda text: all(
            (qk in text) for qk in user_keywords)) 
    elif (cond == 'or'):
        condition = condition & df.Context.apply(lambda text: any(
            (qk in text) for qk in user_keywords))  
    
    df_query = df[condition]
    df_query = df_query.tail(10) 
    
    items = []

    for i in range( len(df_query)):
        item_id = df_query.iloc[i].newsId  
        title = df_query.iloc[i].Title
        content = df_query.iloc[i].Context
        category = df_query.iloc[i].Category
        link = df_query.iloc[i].news_url
        photo_link = df_query.iloc[i].img_url
    
        if pd.isna(photo_link):
            photo_link=""

        item = {
            "id": str(item_id), 
            "category": category, 
            "title": title,
            "content": content, 
            "link": link,
            "photo_link": photo_link,
            "similar_news": get_itemid_most_similar(item_id)
        }

        items.append(item)
    
    return items

def get_news_content(newsId):
    df_item = df[df.newsId == newsId]
    title = df_item.iloc[0].Title   
    content = df_item.iloc[0].Context
    category = df_item.iloc[0].Category
    link = df_item.iloc[0].news_url
    date = df_item.iloc[0].Date
    photo_link = df_item.iloc[0].img_url

    if pd.isna(photo_link):
        photo_link=''

    news_info = {
        "id": str(newsId),
        "category": category,
        "title": title,
        "content": content,
        "link": link,
        "date": date,
        "photo_link": photo_link
    }

    return news_info


def get_topk_news(item_id, news_sim_martrix, topk=3):
    sim_dict = {}
    idx = item_id2idx[item_id]
    for i, value in enumerate(news_sim_martrix[idx]):
        sim_dict[i]=value
    topk_items = sorted(sim_dict.items(), key= itemgetter(1), reverse=True)[:topk+1] 
    topk_items = topk_items[1:] 
    return topk_items

def get_itemid_most_similar(item_id):

    similar_items = get_topk_news(item_id, news_sim_martrix, topk=3)
    items = []
    for idx, score in similar_items:
        item = df.iloc[idx]
        item_id = item.newsId
        title = item.Title
        content = item.Context
        category = item.Category
        link = item.news_url
        photo_link = item.img_url
        # if photo_link value is NaN, replace it with empty string 
        if pd.isna(photo_link):
            photo_link=''

        score = round(float(score), 10)
        item = {
            "category": category, 
            "title": title, 
            "link": link,
            "id": str(item_id), 
            'score': '{:.3f}'.format(score), 
            "photo_link": photo_link
            }
        items.append(item)
    return items