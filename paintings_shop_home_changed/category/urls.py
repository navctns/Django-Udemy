from django.urls import path

from . import views

urlpatterns=[
    path('category/add/',views.create_category,name='create_category'),
    # path('panel/subcategory/add/', views.subcat_add, name='subcat_add'),


]

