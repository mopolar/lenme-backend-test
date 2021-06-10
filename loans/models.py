from django.db import models
# from .views import my_view

class Loan(models.Model):
    username = models.CharField(max_length=200)
    requested_money = models.IntegerField()
    payed_money = models.IntegerField(null=True, blank=True)
    loaner_name = models.CharField(max_length=200, null=True, blank=True)
    lending_time = models.IntegerField()
    loan_status = models.CharField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField('date published', auto_now_add=True, blank=True)
    pay_date = models.DateTimeField('date published', null=True, blank=True)


class Accept(models.Model):
    username = models.CharField(max_length=200)
    requested_money = models.IntegerField(null=True, blank=True)
    precentage = models.IntegerField()
    payed_money = models.IntegerField(null=True, blank=True)
    borrower_name = models.CharField(max_length=200, null=True, blank=True)
    lending_time = models.IntegerField(null=True, blank=True)
    loan_status = models.CharField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField('date published', auto_now_add=True, blank=True)
    pay_date = models.DateTimeField('date published', null=True, blank=True)
    
