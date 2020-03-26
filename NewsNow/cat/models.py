from django.db import models

# Create your models here.



class Cat(models.Model):
     name=models.CharField(max_length=30)
     set_name = models.TextField(default='-')

     def __str__(self):
         return self.set_name

from django.db import models

# Create your models here.
