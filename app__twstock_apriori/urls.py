from django.urls import path
from app__twstock_apriori import views


app_name = 'app__twstock_apriori'

urlpatterns = [
    path('twstockApriori', views.home, name='home'),
    path('iframe/rise', views.iframe_rise, name='rise'),
    path('iframe/fall', views.iframe_fall, name='fall'),

]