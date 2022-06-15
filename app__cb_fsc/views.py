from django.shortcuts import render

def home(request):
    return render(request, 'app__cb_fsc/home.html')
