from django.db import models
import datetime
# Create your models here.

class Post(models.Model):

    picurl1 = models.TextField(default="-")
    picurl2 = models.TextField(default="-")
    picurl3 = models.TextField(default="-")
    post_date = models.DateField()#only one a day