from django.urls import path
from app__overview import views


app_name = 'app__overview'

urlpatterns = [
    path('overview', views.home, name='home'),
    path('api/twstock-latest-news', views.api__latest_new_and_similar_news)
]