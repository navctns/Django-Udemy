from django.urls import path

from . import views

urlpatterns=[
    path('comment/news/add/<pk>/', views.news_cm_add, name='news_cm_add'),

]

