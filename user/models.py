from django.db import models as m

# Create your models here.
class User(m.Model):
    name  = m.CharField(max_length=255)
    email = m.EmailField(unique=True) 