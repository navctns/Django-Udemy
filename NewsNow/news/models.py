from django.db import models

# Create your models here.



class News(models.Model):
     name=models.CharField(max_length=30)
     short_txt=models.TextField()
     body_txt=models.TextField()
     date=models.CharField(max_length=12)
     time=models.CharField(max_length=12,default='00:00')
     picname=models.TextField(max_length=12,default="-")
     picurl=models.TextField(default="-")
     writer=models.CharField(max_length=50)
     catname=models.CharField(max_length=50,default='-')
     catid=models.IntegerField(default=0)
     show=models.IntegerField(default=0)
     ocatid=models.IntegerField(default=0)#maincategory id
     tag=models.TextField(default="")
     act=models.IntegerField(default=0)# For publishting/unpublishing news
     rand = models.IntegerField(default = 0)


     set_name=models.TextField(default='-')


     def __str__(self):
         return self.name

