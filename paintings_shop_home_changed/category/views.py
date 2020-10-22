from django.shortcuts import render
from . models import Category

# Create your views here.


def create_category(request):

    # caterogy=Category.objects.all()
    # print(category)
    if request.method =='POST':

        category_name =request.POST.get('categoryname')
        print('catname', category_name)
        b = Category(name=category_name)
        b.save()

    return render(request, 'back/create_category.html')
