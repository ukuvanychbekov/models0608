from django.contrib import admin
from .models import Customer, Work, Account

# Register your models here.

admin.site.register(Customer)
admin.site.register(Work)
admin.site.register(Account)

