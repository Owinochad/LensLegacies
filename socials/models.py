from django.db import models

# Create your models here.
class SocialUser(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField()
    password = models.CharField(max_length=16)