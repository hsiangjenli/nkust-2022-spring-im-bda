from django.shortcuts import render
import app__api.views as api
from .helper import *
from apyori import apriori
from django.views.decorators.clickjacking import xframe_options_exempt

global df

df = api.df.sort_values(by='Date').tail(1000)

rise_loc, fall_loc = RiseAndFallLoc(df)

Rise = df['tokens_v2'].apply(toList).iloc[rise_loc]
Fall = df['tokens_v2'].apply(toList).iloc[fall_loc]

rise_rule = apriori(transactions=Rise, min_support=support, min_confidence=confidence, min_length=len, max_length=len)
fall_rule = apriori(transactions=Fall, min_support=support, min_confidence=confidence, min_length=len, max_length=len)

rise_outputs = list(rise_rule)
fall_outputs = list(fall_rule)
rise_Source, rise_Target, rise_Weight = cleanRule(rise_outputs)
fall_Source, fall_Target, fall_Weight = cleanRule(fall_outputs)

plotNetwork(rise_Source, rise_Target, rise_Weight, 'rise')
plotNetwork(fall_Source, fall_Target, fall_Weight, 'fall')

def home(request):
    return render(request, 'app__twstock_apriori/home.html')

@xframe_options_exempt
def iframe_rise(request):
    return render(request, 'app__twstock_apriori/rise.html')

@xframe_options_exempt
def iframe_fall(request):
    return render(request, 'app__twstock_apriori/fall.html')
