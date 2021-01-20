
from django.contrib import admin
from django.urls import path, include
from . views import CategoriesView
from . import views

urlpatterns = [
    path('categories/', CategoriesView.as_view()),
    # path('category/add/', AddCategoryFormView.as_view(), name='add_cat'),
    path('', views.add_category, name='add_cat'),
]