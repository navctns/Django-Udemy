
from django.contrib import admin
from django.urls import path, include
from . views import CategoriesView

urlpatterns = [
    path('categories/', CategoriesView.as_view()),
]