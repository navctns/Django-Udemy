from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('about/',views.about,name='about'),
    path('panel/',views.panel,name='panel'),
    path('login/',views.my_login,name='my_login'),
    path('logout/',views.my_logout,name='my_logout'),
    path('panel/setting/', views.site_setting, name='site_setting'),
    path('panel/about/setting/', views.about_setting, name='about_setting'),
    path('contact/',views.contact,name='contact'),
    path('panel/change/pass/', views.change_pass, name='change_pass'),
    path('register/', views.my_register, name='my_register'),

]
