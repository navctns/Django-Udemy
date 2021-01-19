from django.shortcuts import render
from django.views.generic import TemplateView


class PostsView(TemplateView):
    """Main Dashboard view"""

    template_name = "posts1.html"

