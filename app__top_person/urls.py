from django.urls import path
from app__top_person import views


app_name = 'app__top_person'

urlpatterns = [
    path('topPerson', views.home, name='home'),
    path('api/top_person', views.api_post_top_person)
]