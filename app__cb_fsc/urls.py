from django.urls import path
from app__cb_fsc import views


app_name = 'app__cb_fsc'

urlpatterns = [
    path('CentralBankAndFinancialSupervisoryCommission', views.home, name='home'),
]