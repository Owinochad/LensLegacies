from django.contrib import admin
from .models import Blogger, Blog, BlogImage

# Register your models here.

admin.site.register(Blogger)
admin.site.register(Blog)
admin.site.register(BlogImage)

