from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    message = models.TextField(default="-")