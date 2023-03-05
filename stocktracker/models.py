"""
created at: 2023-03-04
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    """
    table for account
    """
    # id
    created_at = models.DateTimeField()
    name = models.CharField(max_length=50)
    name_bank = models.CharField(max_length=20)
    balance = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class AccountHistory(models.Model):
    """
    transection history of Account table
    """
    # id
    created_at = models.DateTimeField()
    # from_account = models.ForeignKey(Account, on_delete=models.PROTECT)
    # to_account = models.ForeignKey(Account, on_delete=models.PROTECT)
    from_account = models.FloatField()
    to_account = models.FloatField()
    amount  = models.IntegerField()
