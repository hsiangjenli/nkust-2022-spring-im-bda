from django.urls import path
from app__overview import views


app_name = 'app__overview'

urlpatterns = [
    path('overview', views.home, name='home'),
]