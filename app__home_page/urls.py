from django.urls import path
from app__home_page import views


app_name = 'app__home_page'

urlpatterns = [
    path('', views.home, name='home'),
    path('api_twii', views.api_twii, name='api_twii')
]