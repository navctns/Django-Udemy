from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User,Group,Permission
import random
from random import randint
import datetime




from manager.models import Manager
from .models import Comment
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from trending.models import Trending
import string

def news_cm_add(request,pk):

    newsname = News.objects.get(pk = pk).name

    # if request.method == 'POST':
    #
    #     comment = request.POST.get('msg')
    #     uname = request.POST.get('name')
    #     email = request.POST.get('email')

    return redirect('news_detail', word=newsname)



