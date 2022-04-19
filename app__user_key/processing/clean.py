from datetime import datetime, timedelta
import pandas as pd
import numpy as np

news_categories = ['tw_stock_news',
                   'tw_macro',
                   'tw_quo',
                   'wd_macro',
                   'us_stock',
                   'eu_asia_stock',
                   'cn_macro',
                   'hk_stock',
                   'sh_stock',
                   '全部']

def filter_dataFrame_fullText(df, user_keywords, cond, cate, weeks):

    # end date: the date of the latest record of news
    end_date = df.Date.max()
    # end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')
    
    start_date = (end_date.date() - timedelta(weeks=weeks)).strftime('%Y-%m-%d')

    # proceed filtering
    if (cate == "全部") & (cond == 'and'):
        df_query = df[(df.Date >= start_date) & (df.Date <= end_date) 
            & df.Context.apply(lambda text: all((qk in text) for qk in user_keywords))]
    elif (cate == "全部") & (cond == 'or'):
        df_query = df[(df['Date'] >= start_date) & (df['Date'] <= end_date) 
            & df.Context.apply(lambda text: any((qk in text) for qk in user_keywords))]
    elif (cond == 'and'):
        df_query = df[(df.Category == cate) 
            & (df.Date >= start_date) & (df.Date <= end_date) 
            & df.Context.apply(lambda text: all((qk in text) for qk in user_keywords))]
    elif (cond == 'or'):
        df_query = df[(df.Category == cate) 
            & (df['Date'] >= start_date) & (df['Date'] <= end_date) 
            & df.Context.apply(lambda text: any((qk in text) for qk in user_keywords))]

    return df_query

def count_keyword(query_df, user_keywords):
    cate_occurence={}
    cate_freq={}

    for cate in news_categories:
        cate_occurence[cate]=0
        cate_freq[cate]=0

    for idx, row in query_df.iterrows():
        # count number of news
        cate_occurence[row.Category] += 1
        cate_occurence['全部'] += 1
        
        # count user keyword frequency by checking every word in tokens_v2
        tokens = np.squeeze(row.tokens_v2).tolist() #row.tokens_v2 #eval(row.tokens_v2)
        freq =  len([word for word in tokens if (word in user_keywords)])
        cate_freq[row.Category] += freq
        cate_freq['全部'] += freq
        
    return cate_freq, cate_occurence
def get_keyword_time_based_freq(df_query):
    date_samples = df_query.Date
    query_freq = pd.DataFrame({'date_index': pd.to_datetime(date_samples), 'freq': [1 for _ in range(len(df_query))]})
    data = query_freq.groupby(pd.Grouper(key='date_index', freq='D')).sum()
    time_data = []
    for i, idx in enumerate(data.index):
        row = {'x': idx.strftime('%Y-%m-%d'), 'y': int(data.iloc[i].freq)}
        time_data.append(row)
    return time_data