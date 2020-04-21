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
from .models import BlackList
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from trending.models import Trending
import string
from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity


def black_list(request):

    ip = BlackList.objects.all()

    return render(request, 'back/blacklist/blacklist.html',{'ip':ip})

def ip_add(request):

    if request.method == "POST":
        ip = request.POST.get('ip')
    if ip != "":
        b = BlackList(ip = ip)
        b.save()

    return redirect('black_list')

def black_list_del(request,pk):

    ip = BlackList.objects.filter(pk=pk)
    ip.delete()

    return redirect('black_list')
