from django import forms

class PDFForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    number = forms.CharField(max_length=15)
    image = forms.ImageField()