from django.urls import path

from . import views

urlpatterns=[
    path('comment/news/add/<pk>/', views.news_cm_add, name='news_cm_add'),
    path('comments/list/', views.comments_list, name='comments_list'),
    path('comments/list/pending', views.comments_list_pending, name='comments_list_pending'),
    path('comments/list/del/<pk>/<num>', views.comments_del, name='comments_del'),
    path('comments/list/confirm/<pk>', views.comments_confirm, name='comments_confirm'),

]

