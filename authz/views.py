from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
# Create your views here.

class Manual(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'authz/main.html')
        loginurl = reverse('login') + '?' + urlencode({'next' : request.path })
        return (redirect(loginurl))

class Protected(View, LoginRequiredMixin):
    def get(self, request):
        return render(request, 'authz/main.html')