from django.contrib import admin
from .models import Account, AssetCash, AssetStock

# Register your models here.
admin.site.register(Account)
admin.site.register(AssetCash)
admin.site.register(AssetStock)
