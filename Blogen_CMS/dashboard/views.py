from django.shortcuts import render
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    """Main Dashboard view"""

    template_name = "dashboard_1.html"

