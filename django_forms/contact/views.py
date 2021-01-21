from django.shortcuts import render, HttpResponse
from .forms import  ContactForm, SnippetForm
# Create your views here.

def contact(request):

    form = ContactForm()

    return render(request, 'form.html',{'form':form})

def snippet_detail(request):

    if request.method == 'POST' :

        form = SnippetForm(request.POST)

        if form.is_valid():
            form.save()
            print("VALID")

    form = SnippetForm()
    return render(request, 'form.html',{'form':form})