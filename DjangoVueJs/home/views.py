from django.shortcuts import render,redirect
import requests
from django.core.files.storage import FileSystemStorage
from . models import Post
import datetime
# Create your views here.


def show_home(request):

    post = Post.objects.get(post_date=datetime.date.today())
    print(post)
    return render(request,'front/vuejsintro.html',{'post':post})

def load_data(request):

    if request.method == 'POST':

        post_date = request.POST.get('date')
        try:
            fs=FileSystemStorage()
            myfile1=request.FILES['myfile1']# myfile from the name of the html input
            filename1=fs.save(myfile1.name,myfile1)
            url1=fs.url(filename1)
            ###img2
            myfile2 = request.FILES['myfile2']  # myfile from the name of the html input
            filename2 = fs.save(myfile2.name, myfile2)
            url2 = fs.url(filename2)
            #img3
            myfile3 = request.FILES['myfile3']  # myfile from the name of the html input
            filename3 = fs.save(myfile3.name, myfile3)
            url3 = fs.url(filename3)

            post = Post(picurl1=url1,picurl2=url2,picurl3=url3,post_date=post_date)
            post.save()

            print(Post.objects.all())

        except:
            print('Input all Images')
        # return redirect('show_home',{'picurl1':url1,'picurl2':url2,'picurl3':url3})

    return render(request,'back/load_data.html')