from django.db import models as m
from django.utils import timezone
import datetime

# Create your models here.

class Blogger(m.Model):
    name = m.CharField(max_length=255)
    username = m.CharField(max_length=255)
    password = m.CharField(max_length=255, default = 'pass1234')
    bio = m.TextField()

    def __str__(self):
        return self.name

class Blog(m.Model):
    title = m.CharField(max_length=255)
    body = m.TextField()
    pub_date = m.DateTimeField("date published")
    blogger = m.ForeignKey(Blogger, on_delete = m.CASCADE)
    image = m.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.title