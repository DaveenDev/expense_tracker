from django.contrib import admin
from .models import Category, Expense

# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['date','description','amount','category']
    list_filter=['date','category']

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category)