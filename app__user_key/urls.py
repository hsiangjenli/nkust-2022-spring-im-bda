from django.urls import path
from app__user_key import views


app_name = 'app__user_key'

urlpatterns = [
    path('userKey', views.home, name='home'),
    path('api/top_userkey/', views.api_get_top_userkey, name='api_get_top_userkey'),
]