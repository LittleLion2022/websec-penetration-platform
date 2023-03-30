from django.db import models

# Create your models here.
class Ports(models.Model):
    username = models.CharField(max_length=20)
    ip = models.GenericIPAddressField()
    portid = models.IntegerField()
    service = models.CharField(max_length=30,default='unknown')
    datetime = models.DateTimeField()