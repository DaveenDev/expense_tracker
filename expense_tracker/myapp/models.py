from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Expense(models.Model):
    date = models.DateField(auto_now=True)
    description = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.description