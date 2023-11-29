from django.contrib import admin
from .models import Cat, Dog, Horse

admin.site.register([Cat, Dog, Horse])