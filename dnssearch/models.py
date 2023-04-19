from django.db import models

# Create your models here.
class Domains(models.Model):
    username = models.CharField(max_length=20)
    domain = models.CharField(max_length=100)
    subdomain = models.CharField(max_length=100,default='')
    count = models.IntegerField(default=0)
    datetime = models.DateTimeField()