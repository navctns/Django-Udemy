from django.shortcuts import render,redirect
import requests
from django.core.files.storage import FileSystemStorage
from . models import Post,IndivPost
import datetime
# Create your views here.


def show_home(request):

    # post = IndivPost.objects.get(post_date=datetime.date.today())
    posts = IndivPost.objects.all()
    print(posts)
    return render(request,'front/vuejsintro.html',{'posts':posts})

def load_data(request):

    if request.method == 'POST':

        post_descr = request.POST.get('descr')
        print(post_descr)
        try:
            fs=FileSystemStorage()
            myfile1=request.FILES['myfile1']# myfile from the name of the html input
            filename1=fs.save(myfile1.name,myfile1)
            url1=fs.url(filename1)
            print('Url1',url1)

            post = IndivPost(picurl=url1,post_desc=post_descr)
            post.save()

            print(IndivPost.objects.all())

        except:
            print('Input all Images')
        # return redirect('show_home',{'picurl1':url1,'picurl2':url2,'picurl3':url3})

    return render(request,'back/load_data.html')