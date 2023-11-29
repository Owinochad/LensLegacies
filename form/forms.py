from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class SimpleForm(forms.Form):
    title = forms.CharField(validators = 
                            [
                                validators.MinLengthValidator(2, 'I need more than 2 characters')
                            ]
                           )
    mileage = forms.IntegerField(validators=[
        validators.MinValueValidator(1, 'I know its not new!')
    ])
    purchase_date = forms.DateField()