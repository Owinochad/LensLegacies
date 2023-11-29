from django.urls import path
from . import views

app_name = 'authz'
urlpatterns = [
    path('', views.Manual.as_view(), name='manual'),
    path('protected/', views.Protected.as_view(), name='Protected'),
]