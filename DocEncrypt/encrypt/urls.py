from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.show_home,name='show_home'),
    path('', views.download_encripted_file, name='download_encripted_file'),

]