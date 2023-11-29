from django.db import models

# Create your models here.
class Lang(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=16)
    lang = models.ForeignKey('Lang', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Instance(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    get_back = models.CharField(max_length=255)

    def __str__(self):
        return self.book