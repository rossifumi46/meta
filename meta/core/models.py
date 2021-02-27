from django.db import models

# Create your models here.

class Method(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Psychoterapist(models.Model):
    name = models.CharField(max_length=30)
    photo = models.URLField(max_length=200)
    methods = models.ManyToManyField(Method)

    def __str__(self):
        return self.name

class Data(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    data = models.TextField()

    def __str__(self):
        return self.date.strftime("%m/%d/%Y, %H:%M:%S")

