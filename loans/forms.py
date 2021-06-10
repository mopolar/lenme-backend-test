from django import forms
from .models import Loan, Accept
  
# creating a form 
class InputForm(forms.ModelForm):
    # username = forms.CharField(max_length=200)
    requested_money = forms.IntegerField()
    # payed_money = forms.IntegerField()
    # loaner_name = forms.CharField(max_length=200)
    lending_time = forms.IntegerField()
    # is_active = forms.BooleanField(default=True)
    class Meta:
        model = Loan
        fields = ['requested_money', 'lending_time']


# creating a form 
class InputForm1(forms.ModelForm):
    precentage = forms.IntegerField()
    class Meta:
        model = Accept
        fields = ['precentage']
