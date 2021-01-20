from django.shortcuts import render
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    """Main Dashboard view"""

    template_name = "dashboard_1.html"

    category_form = ''

    # dispatch is called when the class instance loads
    def dispatch(self, request, *args, **kwargs):

        self.category_form = kwargs.get('category_form', "any_default")

        # needed to have an HttpResponse
        return super(DashboardView, self).dispatch(request, *args, **kwargs)


