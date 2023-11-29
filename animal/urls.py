from django.urls import path
from . import views

app_name = "animal"

urlpatterns = [
    path("", views.CatListView.as_view(), name = "cats"),
    path("horses/", views.HorseListView.as_view(), name="horses"),
    path("dog/", views.DogListView.as_view(), name="dogs"),
    path("add_dog/", views.AddDog.as_view(), name="addDog"),
]