from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from convertdate import french_republican
from cat.models import Cat
from subcat.models import SubCat

def news_detail(request,word):

    site=Main.objects.get(pk=3)
    news=News.objects.filter(name=word)
    return render(request,'front/news_detail.html',{'news':news,'site':site})

def news_list(request):

    news=News.objects.all()
    return render(request,'back/news_list.html',{'news':news})

def news_add(request):
    
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
                    b = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date=today,time=time, picname=filename,
                         picurl=url, writer="-", catname=newsname,
                         catid=newsid, show=0)
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
    try:
        b=News.objects.get(pk=pk)
        fs=FileSystemStorage()
        fs.delete(b.picname)
        b.delete()
    except:
        error="Somethint went Wrong"
        return render(request, 'back/error.html', {'error': error})

    return redirect('news_list')

def news_edit(request,pk):

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
            b.save()
            return redirect('news_list')


        # return redirect('news_list')


    return render(request,'back/news_edit.html',{'pk':pk,'news':news,"cat":cat})