
from django.contrib import admin
from django.contrib.auth.models import  Permission

from .models import Post,IndivPost
# Register your models here.

admin.site.register(Post)
admin.site.register(IndivPost)