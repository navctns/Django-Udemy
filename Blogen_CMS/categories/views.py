from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import AddCategoryForm
from django.views.generic.edit import FormView

class CategoriesView(TemplateView):
    """Main Dashboard view"""

    template_name = "categories1.html"


# class AddCategoryFormView(FormView):
#
#     """Add Category form view"""
#     template_name = 'dashboard_1.html'
#     form_class = AddCategoryForm
#     success_url = "/thanks/"
#
#     def form_valid(self, form):
#         """This method is called when valid data form has been posted
#             It should return an http response
#         """
#         form.create_category()
#         print('create category run')
#         return super().form_valid(form)

def add_category(request):
    """Function based view for model based form"""
    form = AddCategoryForm()

    return render(request, 'dashboard_1.html',{'form':form})
    # return redirect('dashboard',{'form':form})
