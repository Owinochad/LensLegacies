from django import forms

class studentForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    course = forms.BooleanField()