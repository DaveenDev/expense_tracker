from django.shortcuts import redirect, render
from .forms import ExpenseForm
from .models import Expense

# Create your views here.

def index(request):
    
    if request.method=="POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()

    expense_form = ExpenseForm()
    expenses = Expense.objects.all()
    return render(request, "myapp/index.html", {
        'expense_form': expense_form,
        'expenses': expenses
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