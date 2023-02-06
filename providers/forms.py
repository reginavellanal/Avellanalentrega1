from django import forms

class Providerform(forms.Form):
    name = forms.CharField(max_length=100)
    adress = forms.CharField(max_length=300)
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()
