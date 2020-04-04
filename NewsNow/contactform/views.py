from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage





from main.models import Main
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from .models import ContactForm

def contact_add(request):

    if request.method == "POST":

        name=request.POST.get("name")
        email=request.POST.get("email")
        txt=request.POST.get("msg")

        if name =="" or email =="" or txt =="":
            msg="All Fields are required"
            return render(request,'front/contactform/msgbox.html',{'msg':msg})

        b=ContactForm(name=name,email=email,txt=txt)
        b.save()

    msg="Your Message Recieved"


    return render(request,'front/contactform/msgbox.html',{'msg':msg})