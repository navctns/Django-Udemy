from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login,logout




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

    #login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    #login check end
    return render(request,'back/home.html')

def my_login(request):

    if request.method == "POST":

        utxt=request.POST.get('username')
        ptxt=request.POST.get('password')

        if utxt != "" and ptxt != "":

            user=authenticate(username=utxt,password=ptxt)#authenticate() will return none if it is not
            #authenticated, (credentials are wrong)

            if user!= None:
                login(request,user)
                return redirect('panel')


    return render(request,'front/login.html')

def my_logout(request):

    logout(request)

    return redirect('my_login')

def site_setting(request):

    site=Main.objects.get(pk=2)

    return render(request,'back/setting.html',{'site':site})




