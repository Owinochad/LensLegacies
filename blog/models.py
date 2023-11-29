from django.db import models as m
from django.utils import timezone
import datetime

# Create your models here.

class Blogger(m.Model):
    name = m.CharField(max_length=255)
    username = m.CharField(max_length=255)
    bio = m.TextField()

    def __str__(self):
        return self.name

class Blog(m.Model):
    title = m.CharField(max_length=255)
    body = m.TextField()
    pub_date = m.DateTimeField("date published")
    blogger = m.ForeignKey(Blogger, on_delete = m.CASCADE)

    def __str__(self):
        return self.title