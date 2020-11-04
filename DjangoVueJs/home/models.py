from django.db import models
from django.forms import ModelForm
import datetime
# Create your models here.

class Post(models.Model):

    picurl1 = models.TextField(default="-")
    picurl2 = models.TextField(default="-")
    picurl3 = models.TextField(default="-")
    post_date = models.DateField()#only one a day


class IndivPost(models.Model):
    """For a post primary-contains a Picture and a text"""
    picurl = models.TextField(default="-")
    post_desc = models.TextField(default="-")
    likes = models.IntegerField(default=0)

class IndivPost_Form(ModelForm):


    class Meta:
        model = IndivPost
        fields = ('picurl', 'post_desc')



