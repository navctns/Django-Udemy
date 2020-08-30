from django.shortcuts import render
from category.models import Category
from .models import Product
from django.core.files.storage import FileSystemStorage

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

        # b = Product(name=product_name, price=price, categ_id=product_cat)
        # b.save()

        try:

            myfile=request.FILES['myfile']# myfile from the name of the html input
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            url=fs.url(filename)

            if str(myfile.content_type).startswith("image"):


                if myfile.size<5000000:
                    # newsname = SubCat.objects.get(pk=newsid).name
                    # ocatid=SubCat.objects.get(pk=newsid).catid#get catid from subcategory of news
                    # b = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date=today,time=time, picname=filename,
                    #      picurl=url, writer=request.user, catname=newsname,
                    #      catid=newsid, show=0,ocatid=ocatid,tag=tag, rand = rand)
                    # b.save()
                    b = Product(name=product_name, price=price, categ_id=product_cat,picname=filename,picurl=url)
                    b.save()

                    #count of the newses with the ocatid(extracted from subcategory-previous)
                    # count=len(News.objects.filter(ocatid=ocatid))
                    # b=Cat.objects.get(pk=ocatid)#to update count in cat model
                    # b.count=count
                    # b.save()
                    # return redirect('news_list')
                else:
                    error="File is Bigger than 1 MB"
                    return render(request,'back/error.html',{'error':error})

            else:
                fs=FileSystemStorage()
                fs.delete(filename)

                error="Your File Not Supported"
                return render(request,'back/error.html',{'error':error})

        except:
            error = "Please Input Your Image"
            return render(request, 'back/error.html', {'error': error})


    return render(request, 'back/create_product.html', {'category': category})

def product_page(request, pk):

    # shownews=News.objects.filter(name=word)
    # thisproduct = Product.objects.get(pk=pk)
    thisproduct = Product.objects.filter(pk=pk)
    product = Product.objects.get(pk=pk)
    print('this product',thisproduct)
    category = Category.objects.filter(pk=product.categ_id)
    return render(request, 'front/product_page.html',
                  {'thisproduct':thisproduct,'categ':category})

