from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import Blog, BlogImage
class studentForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    course = forms.BooleanField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields =  ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args,**kwargs)
        self.fields['username'].help_text = " "
        self.fields['password1'].help_text = " "
        self.fields['password2'].help_text = " "

class editForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blogger', 'title', 'body']

class BlogForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model= Blog
        fields = ['blogger', 'title', 'body', 'image']

class ImageForm(forms.ModelForm):
    class Meta:
        model = BlogImage
        fields = ['blog', 'image', 'title']




