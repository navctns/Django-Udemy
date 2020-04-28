from django.shortcuts import render,get_object_or_404,redirect
from random import randint

# Create your views here.

from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from convertdate import french_republican
from cat.models import Cat
from subcat.models import SubCat
from trending.models import Trending
from comment.models import Comment
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def news_detail(request,word):

    site=Main.objects.get(pk=3)


    shownews=News.objects.filter(name=word)
    site = Main.objects.get(pk=2)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    trending = Trending.objects.all().order_by('-pk')
    #popular news based on shows
    popnews = News.objects.all().order_by('-show')
    popnews2 = News.objects.all().order_by('-show')[:3]#show only latest 3 items
    tagname=News.objects.get(name=word).tag
    tag=tagname.split(',')
    code = News.objects.get(name=word).pk
    comment = Comment.objects.filter(news_id = code, status = 1).order_by('-pk')[:3]
    cmcount = len(comment)
    try:
        mynews=News.objects.get(name=word)
        mynews.show=mynews.show + 1
        mynews.save()
    except:
        print("Can't add Show")

    link = "/urls/" + str(News.objects.get(name=word).rand)

    return render(request,'front/news_detail.html',{'news':news,'site':site,'cat':cat,
                    'subcat':subcat,'lastnews':lastnews,'shownews':shownews,'popnews':popnews,
                    'popnews2':popnews2,'tag':tag,'trending':trending,'code':code, 'comment':comment,
                    'cmcount':cmcount, 'link':link})

def news_detail_short(request,pk):

    site=Main.objects.get(pk=3)


    shownews=News.objects.filter(rand=pk)
    site = Main.objects.get(pk=2)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    trending = Trending.objects.all().order_by('-pk')
    #popular news based on shows
    popnews = News.objects.all().order_by('-show')
    popnews2 = News.objects.all().order_by('-show')[:3]#show only latest 3 items
    tagname=News.objects.get(rand = pk).tag
    tag=tagname.split(',')
    try:
        mynews=News.objects.get(rand=pk)
        mynews.show=mynews.show + 1
        mynews.save()
    except:
        print("Can't add Show")

    # link =  "/urls/" + str(News.objects.get(rand=pk).rand)

    return render(request,'front/news_detail.html',{'news':news,'site':site,'cat':cat,
                    'subcat':subcat,'lastnews':lastnews,'shownews':shownews,'popnews':popnews,
                    'popnews2':popnews2,'tag':tag,'trending':trending, 'link':link})

def news_list(request):

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
        newss = News.objects.all()
        paginator = Paginator(newss,2)#means a paginator model only two records on a page
        page = request.GET.get('page')
        try :
            news = paginator.page(page)
        except EmptyPage :
            news = paginator.page(paginator.num_page)
        except PageNotAnInteger :
            news = paginator.page(1)

    # end set access to news

    return render(request,'back/news_list.html',{'news':news})

def news_add(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    
    print("-------------------")

    now=datetime.datetime.now()

    print("-------------------")
    year=now.year
    month=now.month
    day=now.day
    hours=now.hour
    minutes=now.minute
    if len(str(month))==1:
        month="0"+str(month)
    if len(str(day))==1:
        day="0"+str(day)

    print(str(year)+ "/" + str(month) + "/" + str(day))
    today=str(year)+ "/" + str(month) + "/" + str(day)
    time=str(hours)+":"+str(minutes)
    print(time)
    date = str(year)+str(month)+str(day)
    randint = str(random.randint(1000,9999))
    rand = date + randint
    rand = int(rand)

    #to avoid repeatation
    while len(News.objects.filter(rand = rand)) != 0:
        randint = str(random.randint(1000, 9999))
        rand = date + randint
        rand = int(rand)



    #now = datetime.datetime.now()-datetime.timedelta(days=10) #get the date before 10 days
    """
    year = now.year
    month = now.month
    day = now.day
    if len(str(month)) == 1:
        month = "0" + str(month)
    if len(str(day)) == 1:
        day = "0" + str(day)

    print(str(year) + "/" + str(month) + "/" + str(day))
    """
    #convert date to french republican

    frdate=french_republican.from_gregorian(int(year),int(month),int(day))
    print(frdate)


    cat=SubCat.objects.all()

    if request.method =='POST':
        newstitle=request.POST.get('newstitle')
        newscat=request.POST.get('newscat')
        newstxtshort=request.POST.get('newstxtshort')
        newstxt=request.POST.get('newstxt')
        newsid=request.POST.get('newscat')
        tag=request.POST.get("tag")


        error="All Fields Required"
        #if newstitle=="" or newscat=="":
            #return render(request, 'back/error.html',{'error':error})

        print(newstitle,newscat,newstxtshort,newstxt)
        try:

            myfile=request.FILES['myfile']# myfile from the name of the html input
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            url=fs.url(filename)

            if str(myfile.content_type).startswith("image"):


                if myfile.size<5000000:
                    newsname = SubCat.objects.get(pk=newsid).name
                    ocatid=SubCat.objects.get(pk=newsid).catid#get catid from subcategory of news
                    b = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date=today,time=time, picname=filename,
                         picurl=url, writer=request.user, catname=newsname,
                         catid=newsid, show=0,ocatid=ocatid,tag=tag, rand = rand)
                    b.save()

                    #count of the newses with the ocatid(extracted from subcategory-previous)
                    count=len(News.objects.filter(ocatid=ocatid))
                    b=Cat.objects.get(pk=ocatid)#to update count in cat model
                    b.count=count
                    b.save()
                    return redirect('news_list')
                else:
                    error="File is Bigger than 1 MB"
                    return render(request,'back/error.html',{'error':error})

            else:
                fs=FileSystemStorage()
                fs.delete(filename)

                error="Your File Not Supported"
                return render(request,'back/error.html',{'error':error})

        except:
            error = "Please Input Your Image"
            return render(request, 'back/error.html', {'error': error})


        #return redirect('news_list')

    return render(request,'back/news_add.html',{'cat':cat})

def news_delete(request,pk):

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
        # to only show news of that writer
        a = News.objects.get(pk = pk).writer
        if str(a) != str(request.user):
            error = "Access Denied"
            return render(request, 'back/error.html', {'error': error})

    # end set access to news

    try:
        b=News.objects.get(pk=pk)
        fs=FileSystemStorage()
        fs.delete(b.picname)
        ocatid=News.objects.get(pk=pk).ocatid#get ocatid(original category id) of the news which deletes

        b.delete()
        #update count of the category after deletion
        count=len(News.objects.filter(ocatid=ocatid))
        m=Cat.objects.get(pk=ocatid)
        m.count=count
        m.save()
    except:
        error="Somethint went Wrong"
        return render(request, 'back/error.html', {'error': error})

    return redirect('news_list')

def news_edit(request,pk):

    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    if len(News.objects.filter(pk=pk))==0:
        error="News Not Found"
        return render(request,'back/error.html',{'error':error})

    news=News.objects.get(pk=pk)

    cat=SubCat.objects.all()




    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscat')
        tag = request.POST.get("tag")

        error = "All Fields Required"
        # if newstitle=="" or newscat=="":
        # return render(request, 'back/error.html',{'error':error})

        print(newstitle, newscat, newstxtshort, newstxt)
        try:

            myfile = request.FILES['myfile']  # myfile from the name of the html input
            fss = FileSystemStorage()
            filename = fss.save(myfile.name, myfile)
            url = fss.url(filename)

            if str(myfile.content_type).startswith("image"):

                if myfile.size < 5000000:
                    newsname = SubCat.objects.get(pk=newsid).name

                    b = News.objects.get(pk=pk)

                    fss = FileSystemStorage()
                    fss.delete(b.picname)

                    b.name=newstitle
                    b.short_txt=newstxtshort
                    b.body_txt=newstxt
                    b.picname=filename
                    b.picurl=url
                    b.catname=newsname
                    b.catid=newsid
                    b.tag=tag
                    b.act=0
                    b.save()
                    return redirect('news_list')
                else:
                    error = "File is Bigger than 1 MB"
                    return render(request, 'back/error.html', {'error': error})

            else:
                #fs = FileSystemStorage()
                #fs.delete(filename)

                error = "Your File Not Supported"
                return render(request, 'back/error.html', {'error': error})

        except:
            newsname = SubCat.objects.get(pk=newsid).name

            b = News.objects.get(pk=pk)
            b.name = newstitle
            b.short_txt = newstxtshort
            b.body_txt = newstxt
            b.catname = newsname
            b.catid = newsid
            b.tag=tag
            b.act=0
            b.save()
            return redirect('news_list')


        # return redirect('news_list')


    return render(request,'back/news_edit.html',{'pk':pk,'news':news,"cat":cat})


def news_publish(request,pk):

    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end
    news = News.objects.get(pk = pk)
    news.act = 1
    news.save()


    return redirect('news_list')

def news_all_show(request, word):

    catid = Cat.objects.get(name=word).pk
    allnews = News.objects.filter(ocatid = catid)

    site = Main.objects.get(pk = 2)
    news = News.objects.filter(act = 1).order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.filter(act = 1).order_by('-pk')[:3]
    popnews = News.objects.filter(act = 1).order_by('-show')
    popnews2 = News.objects.filter(act = 1).order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')
    lastnews2 = News.objects.filter(act = 1).order_by('-pk')[:4]
    random_object = Trending.objects.all()[randint(0, len(trending) - 1)]  # to show random trendings

    return render(request, 'front/all_news.html', {'site': site, 'news': news, "cat": cat, 'subcat': subcat,
                                               'lastnews': lastnews, 'popnews': popnews, 'popnews2': popnews2,
                                               'trending': trending,
                                               'lastnews2': lastnews2, 'allnews':allnews})
