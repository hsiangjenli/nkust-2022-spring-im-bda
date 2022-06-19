from django.urls import path
from app__job104 import views


app_name = 'app__job104'

urlpatterns = [
    path('Job104', views.home, name='home'),
    path('api/job104', views.api_job104)
]