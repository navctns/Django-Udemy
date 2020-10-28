from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render
from django.core.mail import send_mail
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

        return redirect('home')

def delete_contact(request,pk):

    contact = Contact.objects.get(pk=pk)
    contact.delete()

    return redirect('show_all_contacts')

def reply_contact(request,pk):

    if request.method == 'POST':
        contact_reply = request.POST.get('contact_reply')
        print('Reply Message',contact_reply)
        send_mail(
            'Django Test Mail',
            'Sending a Reply mail to contact.',
            'navctns@gmail.com',
            ['navctns@gmail.com'],
            fail_silently=False,
        )

    return redirect('show_all_contacts')


