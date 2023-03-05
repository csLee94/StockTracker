"""
created at: 2023-03-04
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Account, AssetCash, AssetStock
from .forms import AccountForm, AssetCashForm
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
            account.balance = 0
            account.save()
            # create asset_cash
            asset_cash = AssetCash(
                account_id=account,
                created_at = timezone.now(),
                updated_at = timezone.now(),
                user_id = request.user,
                balance=0
            )
            asset_cash.save()
            return redirect("stocktracker:asset_cash_update")
    else:
        form = AccountForm(initial={'balance':0})
    return render(request, 'stocktracker/account_form.html', {'form':form})

@login_required(login_url='common:login')
def asset_cash_update(request):
    """
    update asset_cash
    """
    account_list =  Account.objects.filter(user_id=request.user)
    if request.method == 'POST':
        form = AssetCashForm(request.POST)
        if form.is_valid():
            account = Account.objects.get(id=int(request.POST['account_id']))
            account.balance += int(request.POST['balance'])
            account.save()
            asset_cash = AssetCash.objects.get(account_id=int(request.POST['account_id']))
            asset_cash.updated_at = timezone.now()
            asset_cash.balance = int(request.POST['balance'])
            asset_cash.save()
            return redirect("stocktracker:index")
    else:
        form = AssetCash()
    return render(request, 'stocktracker/asset_cash_form.html', {'form':form, 'account_list':account_list})