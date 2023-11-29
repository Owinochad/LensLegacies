from django.urls import path
from . import views

app_name = 'form'
urlpatterns = [
    path('', views.UserData.as_view(),  name='userdata'),
]