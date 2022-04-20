from django.urls import path
from app__top_freq import views


app_name = 'app__top_freq'

urlpatterns = [
    path('topFreq', views.home, name='home'),
    
]