from django.db import models

# Create your models here.

class Product(models.Model):
     name=models.CharField(max_length=30)
     price = models.FloatField(default=0)
     categ_id=models.IntegerField(default=0)
     categ_name = models.CharField(max_length=30,default="-")
     picname = models.TextField(max_length=12, default="-")
     picurl = models.TextField(default="-")
     artist = models.TextField(max_length=100, default="-")
     description = models.TextField(max_length=200, default="-")


