from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader


from .models import Main
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
# Create your views here.

def index(request):
    sitename="Hello"
    #site=Main.objects.all()
    site=Main.objects.get(pk=1)
    news=News.objects.all().order_by('-pk')
    cat=Cat.objects.all()
    subcat=SubCat.objects.all()
    lastnews=News.objects.all().order_by('-pk')[:3]
    #site=Page.objects.get(pk=1)
    #template=loader.get_template('page/index.html')
    #return HttpResponse("Hello, World You are at news page")
    #return render(request,'page/index.html')
    return render(request, 'front/home.html',{'site':site,'news':news,"cat":cat,'subcat':subcat,'lastnews':lastnews})
    #return HttpResponse(template.render(request))

def about(request):

    site=Main.objects.get(pk=2)
    #sitename="About Page"
    return render(request,'front/about.html',{'site':site})

def panel(request):

    return render(request,'back/home.html')

def my_login(request):

    return render(request,'front/login.html')
