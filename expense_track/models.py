from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    balance = models.FloatField()

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    amount = models.FloatField()
    balance = models.FloatField()
    date = models.CharField(max_length=20)
    to = models.CharField(max_length=20)
    fro = models.CharField(max_length=20)
