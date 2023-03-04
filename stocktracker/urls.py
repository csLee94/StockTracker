"""
created at: 2023-03-04
"""
from django.urls import path

from . import views

app_name = 'stocktracker'

urlpatterns = [
    path('', views.index, name='index'),
]
