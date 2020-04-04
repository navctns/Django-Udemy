from django.db import models

# Create your models here.



class ContactForm(models.Model):

     name=models.CharField(max_length=50)
     email = models.CharField(max_length=50)
     txt=models.TextField()


     set_name = models.TextField(default='-')

     def __str__(self):
         return self.set_name


