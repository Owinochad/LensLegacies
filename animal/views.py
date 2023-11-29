from django.shortcuts import render, redirect
from .models import Dog, Horse, Cat
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView

# Create your views here.
class CatListView(View):
    model = Cat
    def get(self, request):
        model_name = self.model._meta.verbose_name.lower()
        list_objects = self.model.objects.all()
        context = {
            f"{model_name}s": list_objects,
        }
        return render(request, f'animal/{model_name}.html' ,context)

class HorseListView(ListView):
    model = Horse
    model_name = model._meta.verbose_name.title().lower()
    template_name =  "animal/"+ model_name + '.html'
    context_object_name = model_name + "s"


class DogListView(HorseListView):
    model = Dog

class AddDog(View):
    def get(self, request):
        name = request.session.get('name', False)
        if (name) : del(request.session['name'])
        return render(request, 'animal/addDog.html')
    
    def post(self, request):
        name = request.POST.get("dog_name")
        age = request.POST.get("dog_age")
        d = Dog(Name = name, age = age)
        d.save()
        request.session['msg'] = name
        return redirect(request.path)