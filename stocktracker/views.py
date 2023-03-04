"""
created at: 2023-03-04
"""

from django.shortcuts import render
from .models import Account

# Create your views here.

def index(request):
    """
    Index
    """
    account_list = Account.objects.order_by('-balance')
    context = {'account_list':account_list}
    return render(request, 'stocktracker/account_list.html', context)
