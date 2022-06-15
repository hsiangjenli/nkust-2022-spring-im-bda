from django.urls import path
from app__news_classification_bert import views


app_name = 'app__news_classification_bert'

urlpatterns = [
    path('NewsClassificationBert', views.home, name='home'),
    path('api/news_classification_bert', views.api_get_news_category)
]