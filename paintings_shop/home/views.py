from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt# i think:when connecting to other websites(like payment gateway)
from product.models import Product
from category.models import Category
# Create your views here.
@csrf_exempt
def home(request):

    products = Product.objects.all()
    # categories = {}
    #Categories
    categories = Category.objects.all()
    for cat in categories :
        print(cat.name)

    return render(request, 'front/home-page.html',{'products':products})