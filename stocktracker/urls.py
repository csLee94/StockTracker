"""
created at: 2023-03-04
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
