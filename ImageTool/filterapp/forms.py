from django import forms

class ImageFilterForm(forms.Form):
    image = forms.ImageField()
    filter_type = forms.ChoiceField(choices=[
        ('BLUR', 'Blur'),
        ('BW', 'Black & White'),
        ('SHARPEN', 'Sharpen'),
        ('CONTOUR', 'Contuor')
    ])