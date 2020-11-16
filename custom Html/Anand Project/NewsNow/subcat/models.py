from django.db import models

# Create your models here.



class SubCat(models.Model):
     name=models.CharField(max_length=30)
     catname=models.CharField(max_length=30)#of parent category
     catid=models.IntegerField()#of parent category
     set_name = models.TextField(default='-')

     def __str__(self):
         return self.set_name