"""
created at: 2023-03-04
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Account
from .forms import AccountForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# def home(request):
#     """
#     home
#     """
#     account_list = Account.objects.order_by('-balance')
#     context = {'account_list':account_list}
#     return render(request, "stocktracker/index.html", context)

def index(request):
    """
    Index
    """
    if request.user.is_authenticated:
        account_list =  Account.objects.filter(user_id=request.user).order_by('-balance')
    else:
        account_list = None
    context = {'account_list':account_list}
    return render(request, 'stocktracker/index.html', context)

@login_required(login_url='common:login')
def account_create(request):
    """
    create account
    """
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user_id = request.user
            account.created_at = timezone.now()
            account.save()
            return redirect("stocktracker:index")
    else:
        form = AccountForm(initial={'balance':0})
    return render(request, 'stocktracker/account_form.html', {'form':form})