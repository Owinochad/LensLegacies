from django.shortcuts import render, redirect
from django.views import View
from .forms import SimpleForm
# Create your views here.

class UserData(View):

    def get(self, request):
        form = SimpleForm()
        cxt = {'form' : form}
        return render(request, 'form/index.html', cxt)
    
    def post(self, request):
        return redirect(request.path)