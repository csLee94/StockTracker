"""
created at: 2023-03-04
"""

from django.shortcuts import render
from .models import Account

# Create your views here.

def home(request):
    """
    home
    """
    return render(request, "stocktracker/index.html")

def index(request):
    """
    Index
    """
    account_list = Account.objects.order_by('-balance')
    context = {'account_list':account_list}
    return render(request, 'stocktracker/index.html', context)
