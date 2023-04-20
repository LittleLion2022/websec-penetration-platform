from django.db import models

# Create your models here.
class Records(models.Model):
    username = models.CharField(max_length=20)
    keyword = models.CharField(max_length=256,default='')
    app = models.CharField(max_length=256,default='')
    ip = models.GenericIPAddressField()
    country = models.CharField(max_length=256,default='')
    city = models.CharField(max_length=256,default='')
    datetime = models.DateTimeField()