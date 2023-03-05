from django import forms
from stocktracker.models import Account, AssetCash, AssetStock

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'name_bank']
        labels = {
            'name': '계좌 이름',
            'name_bank': '증권사 이름',
        }

class AssetCashForm(forms.ModelForm):
    class Meta:
        model = AssetCash
        fields = ['account_id', 'balance']
        labels = {
            'account_id': '계좌 이름',
            'balance': '잔고',
        }
