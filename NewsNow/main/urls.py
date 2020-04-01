from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('about/',views.about,name='about'),
    path('panel/',views.panel,name='panel'),
    path('login/',views.my_login,name='my_login'),
    path('logout/',views.my_logout,name='my_logout'),
    path('panel/setting/', views.site_setting, name='site_setting'),

]
