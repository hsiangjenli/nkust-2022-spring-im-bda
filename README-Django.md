# Django

## Startup a Project
```python
django-admin startproject website_configs .
```

## Homepage
```
django-admin startapp app__home_page
python manage.py runserver
```

## website_configs/settings.py
```python
ALLOWED_HOSTS = ['*'] # Allow all hosts.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app__home_page', # Add new app.
]

import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Add
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
## Homepage's urls
### Create urls.py at app__home_page
```python
from django.urls import path
from app__home_page import views


app_name = 'app__home_page'

urlpatterns = [
    path('', views.home, name='home'),
]
```
###
```python
from django.contrib import admin
from django.urls import path
from django.urls import include # Add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app__home_page.urls')), # Add
]
```
### Create templates/app__home_page/home.html at app__home_page

## Create a global static folder
### Add these codes at website_configs/settings.py
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
### Create static/images folder
### Load static folder in app__home_page/home.html

```html
{% load static %}
<body>
    <img src="{% static 'images/stock-market.png' %}">
</body>
```
