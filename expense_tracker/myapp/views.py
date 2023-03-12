from django.shortcuts import redirect, render
from django.db.models import Sum
from .forms import ExpenseForm
from .models import Expense
import datetime
# Create your views here.


def calculate_days_expense(no_of_days):
    expenses = Expense.objects.all()

    daterange = datetime.date.today() - datetime.timedelta(days=no_of_days)
    range_expenses = Expense.objects.filter(date__gt=daterange)
    total= range_expenses.aggregate(Sum('amount'))
    return total

def index(request):
    
    if request.method=="POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()
    
    expenses = Expense.objects.all()
    expense_form = ExpenseForm()
    total_expenses = expenses.aggregate(Sum('amount'))

    last_year_expenses = calculate_days_expense(365)
    past_month_expenses = calculate_days_expense(30)
    past_week_expenses= calculate_days_expense(7)
    
    return render(request, "myapp/index.html", {
        'expense_form': expense_form,
        'expenses': expenses,
        'total_expenses': total_expenses,
        'last_year_expenses': last_year_expenses,
        'past_month_expenses': past_month_expenses,
        'past_week_expenses': past_week_expenses
    })


def edit(request,id):
   
    if request.method == "POST":
        expense = Expense.objects.get(pk=id)
        form = ExpenseForm(request.POST, instance=expense)        
        if form.is_valid():
            form.save()
             
            return redirect('home')
    else:
        expense = Expense.objects.get(pk=id)
        expense_form = ExpenseForm(instance=expense)

        return render(request, "myapp/edit.html", {
            'expense_form': expense_form,
            'expense': expense
        })

def delete(request, id):
    if request.method=="POST" and 'delete-form' in request.POST:
        expense = Expense.objects.get(pk=id)
        expense.delete()
    
    return redirect('home')