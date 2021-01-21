from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import AddCategoryForm
from django.views.generic.edit import FormView
from .models import Category
class CategoriesView(TemplateView):
    """Main Dashboard view"""

    template_name = "categories1.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CategoriesView, self).get_context_data(*args, **kwargs)

        cat_objs = Category.objects.all()
        cats = cat_objs
        context["cats"] = cats
        return context

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
    form = AddCategoryForm(request.POST)
    if form.is_valid():
        print("VALID")
        form.save()
    form = AddCategoryForm()

    return render(request, 'dashboard_1.html',{'form':form})
    # return redirect('dashboard',{'form':form})
