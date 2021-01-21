from django.db import models

# Create your models here.

class Category(models.Model):
    """Category Model"""

    title = models.CharField(default="", max_length=50)

    def __str__(self):

        return self.title