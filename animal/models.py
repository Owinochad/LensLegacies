from django.db import models as m

# Create your models here.
class Horse(m.Model):
    Name = m.CharField(max_length=255)
    age = m.IntegerField(default=12)

    def __str__(self):
        return self.Name

class Dog(m.Model):
    Name = m.CharField(max_length=255)
    age = m.IntegerField(default=12)

    def __str__(self):
        return self.Name

class Cat(m.Model):
    Name = m.CharField(max_length=255)
    age = m.IntegerField(default=12)

    def __str__(self):
        return self.Name