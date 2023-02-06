from django import forms

class ProductsForm(forms.Form):
    name = forms.CharField(max_length=100)
    distance = forms.FloatField()
    stock = forms.BooleanField(required=False)

class CategorieForm(forms.Form):
    name = forms.CharField(max_length=50)

class PanaderiaForm(forms.Form):
    name = forms.CharField(max_length=100)
    horario = forms.FloatField()
    stock = forms.BooleanField(required=False)