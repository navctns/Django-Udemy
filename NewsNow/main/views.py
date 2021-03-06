from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User,Group,Permission
import random
from random import randint
import datetime
from rest_framework import viewsets
from .serializer import NewsSerializer
from django.http import JsonResponse



from manager.models import Manager
from .models import Main
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from trending.models import Trending
from newsletter.models import NewsLetter
import string
from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity
from zeep import Client
import requests
import json
from django.views.decorators.csrf import csrf_exempt# i think:when connecting to other websites(like payment gateway)
from bs4 import BeautifulSoup
import urllib.request as urllib2
# Create your views here.

@csrf_exempt
def home(request):
    sitename="Hello"
    #site=Main.objects.all()
    site=Main.objects.get(pk= 2)
    news=News.objects.filter(act=1).order_by('-pk')
    cat=Cat.objects.all()
    subcat=SubCat.objects.all()
    lastnews=News.objects.filter(act=1).order_by('-pk')[:3]
    popnews = News.objects.filter(act=1).order_by('-show')
    popnews2 = News.objects.filter(act=1).order_by('-show')[:3]
    trending=Trending.objects.all().order_by('-pk')
    lastnews2 = News.objects.filter(act=1).order_by('-pk')[:4]
    random_object=Trending.objects.all()[randint(0,len(trending)-1)]#to show random trendings
    print(random_object)

    #zeep
    # client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')
    # result = client.service.ConvertSpeed(
    #     100, 'kilometersPerhour', 'milesPerhour')
    # print('api speed res:',result)
    # assert result == 62.137

    #curl - worked fine
    # b = ''
    # d = ''
    # url ='https://api.covid19api.com/country/south-africa/status/confirmed'
    # payload = {'a':b,'c':d}
    # result = requests.post(url, params = payload)
    # print(result.url)
    # print(result)
    """
    
    PARAMS
    from    2020-03-01T00:00:00Z
    
    to      2020-04-01T00:00:00Z
    
    
    GET By Country All Status
    https://api.covid19api.com/country/south-africa?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z

    """
    # with json
    url = 'https://api.covid19api.com/country/south-africa/status/confirmed'
    data = {'a':'b','c':'d'}
    headers = {'Content-Type':'application/json'}
    result = requests.post(url, data=json.dumps(data), headers=headers)
    print('result json:',result)

    #beautiful soup test
    my_html = """
    <header>
    <title>This is a Test</title>
    </header>
    <p class="para">sample paragraph</p>
    <a href="" name='name' id="name" >abc</a>
    <a href="" name = 'abc' id='abc'>name</a>
    """
    soup = BeautifulSoup(my_html, 'html.parser')
    # print(soup.title)
    # print(soup.title.string)
    # print(soup.title.parent.name)
    # print(soup.p)
    # print(soup.p['class'])#get the class of the tag
    # print(soup.find_all('a'))
    # print(soup.find(id='abc'))

    # url = 'https://www.udemy.com/'
    url = 'http://127.0.0.1:8000/show/data/'
    # result = requests.post(url)
    # print(result.content) #some contents are forbidden(403 Forbidden)
    # soup = BeautifulSoup(result.content,'html.parser')
    # print(soup.title.string)
    opener = urllib2.build_opener()
    content = opener.open(url).read()
    print(content)
    # soup = soup = BeautifulSoup(content,'html.parser')
    # print(soup.title.string)#here we can get the title

    #SESSIONS

    request.session['test'] = 'hello'
    print(request.session['test'])








    #site=Page.objects.get(pk=1)
    #template=loader.get_template('page/index.html')
    #return HttpResponse("Hello, World You are at news page")
    #return render(request,'page/index.html')
    #redirect to a different website, (like a bank gateway)
    # return redirect('https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest#b07f97ba-24f4-4ebe-ad71-97fa35f3b683')

    return render(request, 'front/home.html',{'site':site,'news':news,"cat":cat,'subcat':subcat,
                    'lastnews':lastnews,'popnews':popnews,'popnews2':popnews2,'trending':trending,
                                              'lastnews2':lastnews2})
    #return HttpResponse(template.render(request))

def about(request):



    site = Main.objects.get(pk=2)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popnews = News.objects.all().order_by('-show')
    popnews2 = News.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')
    #sitename="About Page"
    return render(request,'front/about.html',{'site':site,'news':news,"cat":cat,'subcat':subcat,'lastnews':lastnews,'popnews2':popnews2,'trending':trending})

def about_setting(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end
    site = Main.objects.get(pk=2)
    about=Main.objects.get(pk=2).abouttxt

    if request.method == 'POST':

        txt=request.POST.get('txt')

        if txt=="":
            error = "About field can't be empty"
            return render(request, 'back/error.html', {'error': error})
        b=Main.objects.get(pk=2)
        b.abouttxt=txt
        b.save()

    return render(request,'back/about_setting.html',{'about':about,'site':site})

def contact(request):
    site = Main.objects.get(pk=2)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popnews2 = News.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')

    return render(request,'front/contact.html',{'site':site,'news':news,"cat":cat,'subcat':subcat,'lastnews':lastnews,'popnews2':popnews2,'trending':trending})

def panel(request):

    #login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    #login check end

    #checking permission
    perm=0
    perms=Permission.objects.filter(user=request.user)

    for i in perms:
        if i.codename == 'master_user':
            perm=1
    if perm==0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})

    rand = ""
    for i in range(100):
        rand = rand + random.choice(string.ascii_letters)

    #strong password generation

    spec = ['!','@', '$', '%', '^', '&', '*']
    randpass = ""
    i=0
    for i in range(4):
    #while len(randpass)<12:
        #i = i + 1
        r = random.randint(0,3)
        if i == 0 :
            randpass = randpass + random.choice(string.ascii_lowercase)
            randpass += random.choice(string.ascii_lowercase)
            randpass += random.choice(string.ascii_uppercase)
        elif i == 1 :
            randpass += random.choice(string.ascii_lowercase)
            randpass += random.choice(spec)
            randpass += str(random.randint(0,9))
        elif i == 2 :
            randpass += random.choice(string.ascii_uppercase)
            randpass += random.choice(string.ascii_uppercase)
            randpass += str(random.randint(0,9))
        elif i == 3 :
              randpass += random.choice(string.ascii_uppercase)
              randpass += random.choice(spec)
              randpass += random.choice(string.ascii_lowercase)
        #password algorithm end

    count = News.objects.count()#number of newses
    randnews = News.objects.all()[random.randint(0,count-1)]
    humnum = 5300000
    today = datetime.date.today()
    time = datetime.datetime(2020, 4, 18, 12, 42, 0, 665105)
    #time = datetime.time.now()
    now = datetime.datetime.now()

    #time = now.strftime("%H:%M:%S")

    ip, is_routable = get_client_ip(request)#second part is whether it is public(True) or private
    if ip is None:
        ip = "0.0.0.0"
    else:
        if is_routable:
            ipv = "Public"
        else:
            ipv = 'Private'

    print(ip,ipv)




    return render(request,'back/home.html', {'rand':rand,'randpass':randpass,'randnews':randnews,'humnum':humnum,
                                             'today':today, 'time':time})

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
        seo_txt = request.POST.get('seotxt')
        seo_keywords = request.POST.get('seokeywords')
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
        b.seo_txt = seo_txt
        b.seo_keywords = seo_keywords
        if picurl != "-":b.picurl=picurl
        if picname !="-":b.picname=picname
        if picurl2 != "-": b.picurl2 = picurl2
        if picname2 != "-": b.picname2 = picname2
        b.save()




    site=Main.objects.get(pk=2)

    return render(request,'back/setting.html',{'site':site})

def change_pass(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    if request.method == "POST":

        oldpass=request.POST.get("oldpass")
        newpass=request.POST.get("newpass")

        if oldpass =="" or newpass =="":
            error = "All Fields are required"
            return render(request, 'back/error.html', {'error': error})
        print(request.user)
        user=authenticate(username=request.user,password=oldpass)
        if user != None:
            #print("okokokokokok")
            if len(newpass)<8:
                error="Your password must have at least 8 characters"

                return render(request, 'back/error.html', {'error': error})
            count1=0
            count2=0
            count3=0
            count4=0
            for i in newpass:
                if i>="0" and i<="9":
                    count1=1
                if i>="A" and i<="Z":
                    count2=1
                if i>"a" and i<="z":
                    count3=1
                if i>="!" and i<="[":
                    count4=1
            print(count1,count2,count3,count4)
            if count1==1 and count2 ==1 and count3 ==1 and count4 ==1:

                user=User.objects.get(username=request.user)
                user.set_password(newpass)
                user.save()
                return redirect('my_logout')
            else:
                error = "Your password must contain atleast one for each of them(UppserCase,Lowercase,Digit,SpecialCharacter)"

                return render(request, 'back/error.html', {'error': error})


        else:
            error = "Your Password is not correct"
            return render(request, 'back/error.html', {'error': error})
            print("nononononono")


    return render(request,'back/changepass.html')

def my_register(request):

    if request.method =="POST":
        name=request.POST.get('name')
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        print(uname,email,password1,password2)

        ip, is_routable = get_client_ip(request)  # second part is whether it is public(True) or private
        if ip is None:
            ip = "0.0.0.0"
        else:
            if is_routable:
                ipv = "Public"
            else:
                ipv = 'Private'



        if name=="":
            msg = "Enter your Name"
            return render(request, 'front/contactform/msgbox.html', {'msg': msg})


        if len(password1) >= 8:

            #password strength check
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            for i in password1:
                if i >= "0" and i <= "9":
                    count1 = 1
                if i >= "A" and i <= "Z":
                    count2 = 1
                if i > "a" and i <= "z":
                    count3 = 1
                if i >= "!" and i <= "[":
                    count4 = 1
            print(count1, count2, count3, count4)
            if count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1:

                #verify pass
                if password1 != password2:
                    msg = "Your password didn't Match"
                    return render(request, 'front/contactform/msgbox.html', {'msg': msg})

            else:
                msg = "Your Password is not strong"
                return render(request, 'front/contactform/msgbox.html', {'msg': msg})

        else:
            msg = "Your Password Must have Atleast 8 Characters"
            return render(request, 'front/contactform/msgbox.html', {'msg': msg})

        #check for the existing users
        if len(User.objects.filter(username=uname))==0 and len(User.objects.filter(email=email))==0:

            ip, is_routable = get_client_ip(request)  # second part is whether it is public(True) or private
            if ip is None:
                ip = "0.0.0.0"
            try:
                response = DbIpCity.get(ip, api_key='free')
                country = response.country + " | "+response.city
            except:
                counrty = "Unknown"

            #create user
            user=User.objects.create_user(username=uname,email=email,password=password1)
            b=Manager(name=name,utxt=uname,email=email, ip = ip, country = country)
            b.save()

        else:
            msg = "Username or Password is Already Exists"
            return render(request, 'front/contactform/msgbox.html', {'msg': msg})


    return render(request,'front/login.html')

class NewsViewSet(viewsets.ModelViewSet):

    queryset = News.objects.all()
    serializer_class = NewsSerializer

def show_jsondata(request):

    count = NewsLetter.objects.filter(status = 1).count()

    data = {'status':count}

    return JsonResponse(data)



