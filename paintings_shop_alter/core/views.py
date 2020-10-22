from django.shortcuts import render
from category.models import Category
from product.models import Product
from django.core.files.storage import FileSystemStorage

# Create your views here.
def backend_dashboard(request):

    return render(request,'back/dashboard_master.html')

def create_new_product(request):

    category=Category.objects.all()

    if request.method =='POST':

        product_name =request.POST.get('productname')
        price =request.POST.get('productprice')
        product_cat=request.POST.get('productcat')
        artist_name = request.POST.get('artist_name')
        description_inp = request.POST.get('description')

        categ_name = Category.objects.get(pk=product_cat).name
        # newstxtshort=request.POST.get('newstxtshort')
        # newstxt=request.POST.get('newstxt')
        # newsid=request.POST.get('newscat')
        # tag=request.POST.get("tag")

        # b = Product(name=product_name, price=price, categ_id=product_cat)
        # b.save()

        try:

            myfile=request.FILES['myfile']# myfile from the name of the html input
            print('File inputed', myfile)
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            url=fs.url(filename)

            if str(myfile.content_type).startswith("image"):


                if myfile.size<5000000:
                    print('File Size Ok')
                    # newsname = SubCat.objects.get(pk=newsid).name
                    # ocatid=SubCat.objects.get(pk=newsid).catid#get catid from subcategory of news
                    # b = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date=today,time=time, picname=filename,
                    #      picurl=url, writer=request.user, catname=newsname,
                    #      catid=newsid, show=0,ocatid=ocatid,tag=tag, rand = rand)
                    # b.save()
                    print('Product datas',product_name,price,product_cat,filename,url,artist_name,description_inp,categ_name)
                    b = Product(name=product_name, price=price, categ_id=product_cat,picname=filename,picurl=url,
                                artist=artist_name,categ_name=categ_name)
                    b.save()

                    all_products = Product.objects.all()
                    print("ALL Products",all_products)
                    #count of the newses with the ocatid(extracted from subcategory-previous)
                    # count=len(News.objects.filter(ocatid=ocatid))
                    # b=Cat.objects.get(pk=ocatid)#to update count in cat model
                    # b.count=count
                    # b.save()
                    return redirect('get_products_list')
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


    # return render(request, 'back/create_product.html', {'category': category})
    return render(request, 'back/create_product_alter.html', {'category': category})


def dashboard_main(request):

    return render(request, 'back/dashboard_master.html')

def get_products_list(request):

    products = Product.objects.all()

    return render(request, 'back/all_products_list.html',{'products':products})