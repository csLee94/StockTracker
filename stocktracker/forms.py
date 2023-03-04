from django import forms
from stocktracker.models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'name_bank', 'balance']
        labels = {
            'name': '계좌 이름',
            'name_bank': '증권사 이름',
            'balance': '잔고',
        }
