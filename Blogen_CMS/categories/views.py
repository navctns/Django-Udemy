from django.shortcuts import render
from django.views.generic import TemplateView


class CategoriesView(TemplateView):
    """Main Dashboard view"""

    template_name = "categories1.html"

