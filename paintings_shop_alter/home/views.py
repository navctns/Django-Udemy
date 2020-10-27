from django.shortcuts import render
import requests
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt# i think:when connecting to other websites(like payment gateway)
from product.models import Product
from category.models import Category
# Create your views here.
@csrf_exempt
def home(request):

    products = Product.objects.all()
    # categories = {}
    categories = Category.objects.all()
    paintings = []
    sculptures = []
    # for cat in categories:
    #     print(cat.name)
    #     if cat.name == 'Paintings':
    #         paintings = Product.objects.get(categ_id = cat.pk)
    # product_by_cat = Product.objects.values('category__name')
    # print(product_by_cat)
    # products_by_cat = UserExtendedProfile.objects.values('company', 'user').order_by('company')
    # paintings = get_object_or_404(Product, categ_name='Paintings')
    paintings = list(Product.objects.filter(categ_name='Paintings'))
    sculptures = list(Product.objects.filter(categ_name='Sculptures'))
    products_by_cat = Product.objects.values('name', 'categ_id').order_by('categ_id')
    print('PRODUCT CATEG WISE', products_by_cat)
    return render(request, 'front/home-page.html',{'products':products,'paintings':paintings,'sculptures':sculptures})