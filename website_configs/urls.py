"""website_configs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app__home_page.urls')),
    path('', include('app__overview.urls')),
    path('', include('app__user_key.urls')),
    path('', include('app__top_person.urls')),
    path('', include('app__api.urls')),
    path('', include('app__user_key_sentiment.urls')),
    path('', include('app__twstock_apriori.urls')),
    path('', include('app__cb_fsc.urls')),
    path('', include('app__news_classification_bert.urls')),
    path('', include('app__fullcontext_search.urls')),
]