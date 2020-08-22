from django.shortcuts import render
from category.models import Category
from .models import Product

# Create your views here.


def create_product(request):

    category=Category.objects.all()

    if request.method =='POST':

        product_name =request.POST.get('productname')
        price =request.POST.get('productprice')
        product_cat=request.POST.get('productcat')

        # newstxtshort=request.POST.get('newstxtshort')
        # newstxt=request.POST.get('newstxt')
        # newsid=request.POST.get('newscat')
        # tag=request.POST.get("tag")

        b = Product(name=product_name, price=price, categ_id=product_cat)
        b.save()


    return render(request, 'back/create_product.html', {'category': category})
