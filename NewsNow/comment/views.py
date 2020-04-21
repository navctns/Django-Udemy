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

    #date and time

    now = datetime.datetime.now()

    print("-------------------")
    year = now.year
    month = now.month
    day = now.day
    hours = now.hour
    minutes = now.minute
    if len(str(month)) == 1:
        month = "0" + str(month)
    if len(str(day)) == 1:
        day = "0" + str(day)

    print(str(year) + "/" + str(month) + "/" + str(day))
    today = str(year) + "/" + str(month) + "/" + str(day)
    time = str(hours) + ":" + str(minutes)



    newsname = News.objects.get(pk = pk).name

    if request.method == 'POST':

        cm = request.POST.get('msg')

        if request.user.is_authenticated:
            manager = Manager.objects.get(utxt = request.user)
            b = Comment(name = manager.name, email = manager.email, cm = cm, news_id = pk, date = today,
                        time = time)
            b.save()
        else :
            name = request.POST.get('name')
            email = request.POST.get('email')
            b = Comment(name = name, email = email, cm = cm, news_id = pk, date = today, time = time)
            b.save()

        # uname = request.POST.get('name')
        # email = request.POST.get('email')

    return redirect('news_detail', word = newsname)
    #return redirect('news_detail', word=newsname)

def comments_list(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    # set access to news
    perm = 0
    for i in request.user.groups.all():

        if i.name == "masteruser":
            perm = 1
    if perm == 0:
        news = News.objects.filter(writer=request.user)
    elif perm == 1:
        news = News.objects.all()
    # end set access to news
    #comment = Comment.objects.all()
    comment = Comment.objects.filter(status = 1)


    return render(request, 'back/comments/comments_list.html', {'comment':comment})

def comments_list_pending(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    # set access to news
    perm = 0
    for i in request.user.groups.all():

        if i.name == "masteruser":
            perm = 1
    if perm == 0:
        news = News.objects.filter(writer=request.user)
    elif perm == 1:
        news = News.objects.all()
    # end set access to news
    #comment = Comment.objects.all()
    pcomment = Comment.objects.filter(status = 0)


    return render(request, 'back/comments/pending_comments.html', {'pcomment':pcomment})

def comments_del(request,pk,num):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    # set access to news
    # perm = 0
    # for i in request.user.groups.all():
    #
    #     if i.name == "masteruser":
    #         perm = 1
    # if perm == 0:
    #     news = News.objects.filter(writer=request.user)
    # elif perm == 1:
    #     news = News.objects.all()
    # end set access to news
    comment = Comment.objects.filter(pk=pk)
    comment.delete()

    if int(num) == 1:
        return redirect('comments_list')

    else:
        return redirect('comments_list_pending')



def comments_confirm(request,pk):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    # set access to news
    # perm = 0
    # for i in request.user.groups.all():
    #
    #     if i.name == "masteruser":
    #         perm = 1
    # if perm == 0:
    #     news = News.objects.filter(writer=request.user)
    # elif perm == 1:
    #     news = News.objects.all()
    # end set access to news
    comment = Comment.objects.get(pk=pk)
    comment.status = 1
    comment.save()

    return redirect('comments_list_pending')
