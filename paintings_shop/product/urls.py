from django.urls import path

from . import views

urlpatterns=[
    path('product/add/',views.create_product,name='create_product'),
    # path('panel/subcategory/add/', views.subcat_add, name='subcat_add'),


]

