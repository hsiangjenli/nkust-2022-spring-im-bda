from django.urls import path
from app__user_key_sentiment import views


app_name = 'app__user_key_sentiment'

urlpatterns = [
    path('userKeySentiment', views.home, name='home'),
    path('api/get_userkey_sentiment', views.api_get_userkey_sentiment),
]