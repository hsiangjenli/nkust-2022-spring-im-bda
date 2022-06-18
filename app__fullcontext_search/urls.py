
from django.urls import path
from app__fullcontext_search import views


app_name = 'app__fullcontext_search'

urlpatterns = [
    path('FullContextSearch', views.home, name='home'),
    path('api/fullcontext_search', views.api_fullcontext_search),
]