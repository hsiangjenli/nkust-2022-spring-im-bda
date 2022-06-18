from django.urls import path
from app__news_recommend_bert import views


app_name = 'app__news_recommend_bert'

urlpatterns = [
    path('NewsRecommendBert', views.home, name='home'),
    path('api/LatestNews', views.latestnews),
]