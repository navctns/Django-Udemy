from django.urls import path

from . import views

urlpatterns=[
    path('get/message',views.get_message,name='get_message'),
    path('delete/contact/<pk>', views.delete_contact, name='delete_contact'),
    path('reply/contact/<pk>', views.reply_contact, name='reply_contact'),

]

