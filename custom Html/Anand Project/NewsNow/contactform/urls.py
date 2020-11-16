from django.urls import path

from . import views

urlpatterns=[
    path('contact/submit', views.contact_add, name='contact_add'),
    path('panel/contactform/', views.contact_show, name='contact_show'),
    path('panel/contactform/del/<pk>', views.contact_del, name='contact_del'),
    path('panel/answer/comments/<pk>/', views.answer_cm, name='answer_cm'),

]

