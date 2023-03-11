from .models import Expense
from django.forms import ModelForm

class ExpenseForm(ModelForm):
    class Meta:
      model = Expense
      fields = ('description','amount', 'category')
      