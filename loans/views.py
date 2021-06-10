import user
from loans.models import Loan, Accept
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import InputForm, InputForm1
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from datetime import date
from dateutil.relativedelta import relativedelta
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# from ..user.models import User

User = get_user_model()

def loan(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.username = request.user.username
            recipe.loan_status = 'Not Funded'
            # recipe.loan_status = 'Not Funded'
            recipe.save()
            return redirect('/')
    else:
        form = InputForm()
    return render(request, 'user/register.html', {'form': form,'title':'request loan'})


def accept(request, id):
    if request.method == 'POST':
        form = InputForm1(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.username = request.user.username
            requestmoney = Loan.objects.get(id=id)
            recipe.borrower_name = requestmoney.username
            recipe.requested_money = requestmoney.requested_money
            recipe.loan_status = 'Not Funded'
            recipe.payed_money = (requestmoney.requested_money) + ((requestmoney.requested_money)*((form.cleaned_data.get('precentage')/12)*requestmoney.lending_time*0.01))
            recipe.lending_time = requestmoney.lending_time
            recipe.save()
            return redirect('/table/')
    else:
        form = InputForm1()
    return render(request, 'user/accept.html', {'form': form, 'balance': int(request.user.balance), 'requested': int(Loan.objects.get(id=id).requested_money)+3, 'title':'request loan'})


def display_loans(request):
    try:
        query_results = Loan.objects.filter(loan_status='Not Funded')
    except:
        query_results = {}
    return render(request, 'user/table.html', {'query_results': query_results, 'title':'request loan'})


def display_accepts(request):
    query_results = Accept.objects.filter(borrower_name=request.user.username)
    return render(request, 'user/table1.html', {'query_results': query_results, 'title':'request loan'})


def display_done(request):
    query_results = Accept.objects.filter(username=request.user.username)
    return render(request, 'user/table2.html', {'query_results': query_results, 'title':'request loan'})


def final(request, id):
    # if request.method == 'POST':
    lender = Accept.objects.filter(id=id).first()
    borrow = Loan.objects.filter(username=lender.borrower_name).first()
    lender.loan_status = 'Funded'
    lender.pay_date = date.today() + relativedelta(months=+6)   
    lender.save()
    borrow.payed_money = lender.payed_money
    borrow.loaner_name = lender.username
    borrow.loan_status = 'Funded'
    borrow.pay_date = date.today() + relativedelta(months=+6)
    borrow.save()
    current_user = User.objects.filter(id=request.user.id).first()
    current_user.balance =  int(current_user.balance) + int(borrow.requested_money)
    current_user.save()
    other_user = User.objects.filter(username=lender.username).first()
    other_user.balance = int(other_user.balance) - int(borrow.requested_money) - 3
    other_user.save()
    return redirect('/response/')



def pay(request, id):
    # if request.method == 'POST':
    lender = Accept.objects.filter(id=id).first()
    borrow = Loan.objects.filter(username=lender.borrower_name).first()
    lender.loan_status = 'Completed'
    lender.save()
    borrow.loan_status = 'Completed'
    borrow.save()
    current_user = User.objects.filter(id=request.user.id).first()
    current_user.balance =  int(current_user.balance) - int(lender.payed_money)
    current_user.save()
    other_user = User.objects.filter(username=lender.username).first()
    other_user.balance = int(other_user.balance) + int(lender.payed_money)
    other_user.save()
    return redirect('/response/')