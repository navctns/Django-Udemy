from django.urls import path

from . import views

urlpatterns=[
    path('panel/blacklist/', views.black_list, name='black_list'),
    path('panel/blacklist/add', views.ip_add, name='ip_add'),
    path('panel/blacklist/del/<pk>', views.black_list_del, name='black_list_del'),

]

