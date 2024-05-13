from django.contrib import admin

from .models import ExchangeRate, Currency

admin.site.register(Currency)
admin.site.register(ExchangeRate)
