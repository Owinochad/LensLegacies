from django.shortcuts import render, redirect
from .models import SocialUser
from django.views import View
# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, "socials/home.html")
    def post(self, request):
        return redirect(request.path)