from django.urls import path

from . import views

urlpatterns=[
  #path('news/(?P<word>\dt)/$',views.news_detail,name='news_detail'),
  path('news/<word>',views.news_detail,name='news_detail'),
  path('panel/news/list/',views.news_list,name='news_list'),
  path('panel/news/add/',views.news_add,name='news_add'),
  path('panel/news/del/<pk>',views.news_delete,name='news_delete'),
  path('panel/news/edit/<pk>',views.news_edit,name='news_edit'),
  path('panel/news/publish/<pk>', views.news_publish, name='news_publish'),
  path('urls/<pk>', views.news_detail_short, name='news_detail_short'),
  path('all/news/<word>/', views.news_all_show, name='news_all_show'),
  path('all/news/', views.all_news, name='all_news'),
  path('search/', views.all_news_search, name='all_news_search'),

]


