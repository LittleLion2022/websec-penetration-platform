from django.db import models

# Create your models here.
class Dirs(models.Model):
    username = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    dir = models.CharField(max_length=100,default='/')
    httpcode = models.IntegerField()
    datetime = models.DateTimeField()