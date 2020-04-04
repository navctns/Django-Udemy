from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
import datetime





from main.models import Main
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from .models import ContactForm

def contact_add(request):
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

    if request.method == "POST":

        name=request.POST.get("name")
        email=request.POST.get("email")
        txt=request.POST.get("msg")

        if name =="" or email =="" or txt =="":
            msg="All Fields are required"
            return render(request,'front/contactform/msgbox.html',{'msg':msg})

        b=ContactForm(name=name,email=email,txt=txt,date=today,time=time)
        b.save()

    msg="Your Message Recieved"


    return render(request,'front/contactform/msgbox.html',{'msg':msg})

def contact_show(request):

    """show list of contacts, email,messages"""

    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    msg=ContactForm.objects.all()

    return render(request, 'back/contactform/contact_form.html',{'msg':msg})

def contact_del(request,pk):

    """"Delete records in contact list"""

    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    b=ContactForm.objects.filter(pk=pk)
    b.delete()

    return redirect('contact_show')

