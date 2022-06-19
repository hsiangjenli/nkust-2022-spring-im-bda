from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from apyori import apriori
from .helper import *


df = LoadPyMongo()
list_Transaction = DataFrameToTransaction(df_FromMongoDB=df)

def home(request):
    return render(request, 'app__job104/home.html')

@csrf_exempt
def api_job104(request):
    support = request.POST.get('support')
    AprioriRule = apriori(
        transactions=list_Transaction,
        min_support=float(support), 
        min_confidence=0.6, 
        min_length=2, 
        max_length=2
    )
    list_From, list_To = ExtractRule(APRIORI_RULE=AprioriRule)
    list_JS_Nodes, list_JS_Edges = ToJsResponse(list_From, list_To)
    return JsonResponse({'Nodes': list_JS_Nodes, 'Edges': list_JS_Edges})