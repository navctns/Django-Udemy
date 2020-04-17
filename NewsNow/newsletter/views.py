from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

from .models import NewsLetter
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from convertdate import french_republican
from cat.models import Cat
from subcat.models import SubCat
from trending.models import Trending

def news_letter(request):

    if request.method == 'POST':

        txt = request.POST.get('txt')
        res = txt.find('@') #check for wheter char @ in the input

        if int(res) != -1 :

            b = NewsLetter(txt = txt, status = 1)
            b.save()
        else:

            try:
                int(txt)
                b = NewsLetter(txt=txt, status=2)
                b.save()
            except:
                return redirect('home')


    return redirect('home')

def news_emails(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    emails = NewsLetter.objects.filter(status = 1)

    return render(request, 'back/newsletter/emails.html', {'emails':emails})

def news_phones(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    phones = NewsLetter.objects.filter(status = 2)

    return render(request, 'back/newsletter/phones.html', {'phones':phones})

def news_txt_del(request, pk, num):

    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    b = NewsLetter.objects.get(pk = pk)
    b.delete()

    if int(num) == 2 :
        return redirect('news_phones')

    else:
        return redirect('news_emails')
