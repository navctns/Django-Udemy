
from django.contrib import admin
from django.urls import path, include
from . views import CategoriesView
from . import views

urlpatterns = [
    path('categories/', CategoriesView.as_view(), name="cat_list"),
    # path('category/add/', AddCategoryFormView.as_view(), name='add_cat'),
    path('', views.add_category, name='add_cat'),
    path('delete/<pk>', views.delete_category, name='delete_cat'),
    path('search/', views.search_category, name='search_cat'),

]