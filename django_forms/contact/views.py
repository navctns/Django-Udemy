from django.shortcuts import render, HttpResponse
from .forms import  ContactForm
# Create your views here.

def contact(request):

    form = ContactForm()

    return render(request, 'form.html',{'form':form})