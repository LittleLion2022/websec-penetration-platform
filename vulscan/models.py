from django.db import models

# Create your models here.
class Vuls(models.Model):
    username = models.CharField(max_length=20)
    url = models.CharField(max_length=30)
    vul = models.CharField(max_length=30)
    vul_id = models.CharField(max_length=30)
    grade = models.IntegerField(default=0)
    datetime = models.DateTimeField()