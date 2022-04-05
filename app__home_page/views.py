from django.shortcuts import render
from django.http import  JsonResponse, HttpResponse
import csv


def home(request):
    return render(request, 'app__home_page/home.html')

def api_twii(request):
    with open('app__home_page/dataset/twii.csv', encoding = 'utf-8') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=app__home_page/dataset/twii.csv'
        print(response)
        return response


