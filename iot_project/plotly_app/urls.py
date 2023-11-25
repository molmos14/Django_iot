# your_app_name/urls.py
from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view, name='home_view'),
]

