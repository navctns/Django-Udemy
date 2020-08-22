from django.db import models

# Create your models here.

class Product(models.Model):
     name=models.CharField(max_length=30)
     price = models.FloatField(default=0)
     categ_id=models.IntegerField(default=0)
