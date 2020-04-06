from django.db import models

# Create your models here.



class Trending(models.Model):

     #trending text on topbar
     txt=models.CharField(max_length=200)


     def __str__(self):
         return self.txt


