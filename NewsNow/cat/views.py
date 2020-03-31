from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

from .models import Cat

def cat_list(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    cat=Cat.objects.all()
    return render(request,'back/cat_list.html',{'cat':cat})

def cat_add(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    if request.method=='POST':
        name=request.POST.get('name')
        if name=="":
            error="Empty Field!!!"
            return render(request,'back/error.html')
        b=Cat(name=name)
        b.save()
        return redirect('cat_list')

    return render(request,'back/cat_add.html')