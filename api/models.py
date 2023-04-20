from django.db import models

# Create your models here.
class APIs(models.Model):
    username = models.CharField(max_length=20)
    vt_key = models.CharField(max_length=256,default='')
    av_key = models.CharField(max_length=256,default='')
    ze_key = models.CharField(max_length=256,default='')

