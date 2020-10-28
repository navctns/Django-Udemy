from django.urls import path

from . import views

urlpatterns=[
    path('get/message',views.get_message,name='get_message'),

]

