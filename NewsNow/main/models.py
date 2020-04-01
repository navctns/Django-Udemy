from django.db import models

# Create your models here.



class Main(models.Model):
     name=models.CharField(max_length=30)
     about=models.TextField()
     fb=models.CharField(default='-',max_length=30)
     tw=models.CharField(default='-',max_length=30)
     yt=models.CharField(default='-',max_length=30)
     tell=models.CharField(default='-',max_length=30)
     link=models.CharField(default='-',max_length=30)
     picurl=models.TextField(default="")
     picname=models.TextField(default="")

     set_name=models.TextField(default='-')


     def __str__(self):
         return self.set_name + " | " + str(self.pk)

