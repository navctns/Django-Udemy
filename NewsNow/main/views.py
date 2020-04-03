from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage





from .models import Main
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
# Create your views here.

def index(request):
    sitename="Hello"
    #site=Main.objects.all()
    site=Main.objects.get(pk=2)
    news=News.objects.all().order_by('-pk')
    cat=Cat.objects.all()
    subcat=SubCat.objects.all()
    lastnews=News.objects.all().order_by('-pk')[:3]
    popnews = News.objects.all().order_by('-show')
    popnews2 = News.objects.all().order_by('-show')[:3]
    #site=Page.objects.get(pk=1)
    #template=loader.get_template('page/index.html')
    #return HttpResponse("Hello, World You are at news page")
    #return render(request,'page/index.html')
    return render(request, 'front/home.html',{'site':site,'news':news,"cat":cat,'subcat':subcat,'lastnews':lastnews,'popnews':popnews,'popnews2':popnews2})
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



    if request.method == 'POST':

        name=request.POST.get('name')
        tell=request.POST.get('tell')
        fb=request.POST.get('fb')
        tw=request.POST.get('tw')
        yt=request.POST.get('yt')
        link=request.POST.get('link')
        txt=request.POST.get('txt')

        if fb == "" : fb="#"
        if tw == "": tw = "#"
        if yt == "": yt = "#"
        if link == "": link = "#"

        if name =="" or tell =="" or txt =="":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error': error})

        try:
            myfile = request.FILES['myfile']  # myfile from the name of the html input
            fss = FileSystemStorage()
            filename = fss.save(myfile.name, myfile)
            url = fss.url(filename)

            if str(myfile.content_type).startswith("image"):

                if myfile.size < 5000000:

                    #b = Main.objects.get(pk=2)



                    picurl=url
                    picname=filename


                else:
                    error = "File is Bigger than 1 MB"
                    return render(request, 'back/error.html', {'error': error})

            else:
                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Your File Not Supported"
                return render(request, 'back/error.html', {'error': error})

        except:
            picurl="-"
            picname="-"

        #for the logo image input on the footer
        try:
            myfile2 = request.FILES['myfile2']  # myfile from the name of the html input
            fss2 = FileSystemStorage()
            filename2 = fss2.save(myfile2.name, myfile2)
            url2 = fss2.url(filename2)

            if str(myfile2.content_type).startswith("image"):

                if myfile2.size < 5000000:


                    picurl2=url2
                    picname2=filename2


                else:
                    error = "File is Bigger than 1 MB"
                    return render(request, 'back/error.html', {'error': error})

            else:
                fs = FileSystemStorage()
                fs.delete(filename2)

                error = "Your File Not Supported"
                return render(request, 'back/error.html', {'error': error})

        except:
            picurl2="-"
            picname2="-"

        b=Main.objects.get(pk=2)
        b.name=name
        b.tell=tell
        b.fb=fb
        b.tw=tw
        b.yt=yt
        b.link=link
        b.about=txt
        if picurl != "-":b.picurl=picurl
        if picname !="-":b.picname=picname
        if picurl2 != "-": b.picurl2 = picurl2
        if picname2 != "-": b.picname2 = picname2
        b.save()




    site=Main.objects.get(pk=2)

    return render(request,'back/setting.html',{'site':site})




