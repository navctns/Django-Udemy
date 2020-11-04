from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[
    path('',views.dashboard_main,name="dashboard_main"),
    path('dashboard/product/new/', views.create_new_product, name='create_new_product'),
    path('dashboard/product/list/', views.get_products_list, name='get_products_list'),
    path('dashboard/', views.backend_dashboard, name='backend_dashboard'),
    path('dashboard/edit/product/<pk>', views.edit_product, name='edit_product'),
    path('dashboard/delete/product/<pk>', views.delete_product, name='delete_product'),
    path('dashboard/contacts/list/', views.show_all_contacts, name='show_all_contacts'),
    path('login/', views.goto_login, name='goto_login'),
    path('logout/', views.goto_logout, name='goto_logout'),

    # path('about/',views.about,name='about'),

]
