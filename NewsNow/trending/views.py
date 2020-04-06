from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage

from .models import Trending
from news.models import News
from cat.models import Cat
from subcat.models import SubCat

def trending_add(request):

    if request.method =="POST":

        txt=request.POST.get("txt")

        if txt =="":
            error = "field is empty"
            return render(request, 'back/error.html', {'error': error})
        b=Trending(txt=txt)
        b.save()
    trending_list=Trending.objects.all()

    return render(request,'back/trending/trending.html',{'trending_list':trending_list})

def trending_del(request,pk):

    #delete trending entry
    b=Trending.objects.filter(pk=pk)
    b.delete()

    return redirect('trending_add')

def trending_edit(request,pk):

    txt=Trending.objects.get(pk=pk).txt

    if request.method =="POST":

        txt=request.POST.get('mytxt')

        if txt =="":
            error = "Field is Empty"
            return render(request, 'back/error.html', {'error': error})
        b=Trending.objects.get(pk=pk)
        b.txt=txt
        b.save()
        return redirect('trending_add')

    return render(request,'back/trending/trending_edit.html',{'txt':txt,'pk':pk})