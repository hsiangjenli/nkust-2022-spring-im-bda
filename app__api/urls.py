from django.urls import path
from app__api import views


app_name = 'app__api'

urlpatterns = [
    path('api/twii_5_mins', views.api_twii_5mins, name='api_twii_5mins'),
]