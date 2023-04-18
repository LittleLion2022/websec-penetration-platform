from django.db import models

# Create your models here.
class Domins(models.Model):
    username = models.CharField(max_length=20)
    domin = models.CharField(max_length=100)
    subdomin = models.CharField(max_length=100,default='/')
    datetime = models.DateTimeField()