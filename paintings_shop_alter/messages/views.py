from django.shortcuts import render

# Create your views here.
from . models import Contact

def get_message(request):

    if request.method =='POST':
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_message = request.POST.get('contact_message')

        contact_obj = Contact(contact_name = contact_name, email = contact_email, \
                              message = contact_message)

        contact_obj.save()