"""
created at: 2023-03-04
"""
from django.urls import path

from . import views

app_name = 'stocktracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.index),
    path('account/create/', views.account_create, name='account_create')
]
