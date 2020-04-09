from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User,Group,Permission


from .models import Manager
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from trending.models import Trending

def manager_list(request):

    manager=Manager.objects.all()

    return render(request,'back/manager/manager_list.html',{'manager':manager})

def manager_del(request,pk):


    manager=Manager.objects.get(pk=pk)
    b=User.objects.filter(username=manager.utxt)
    b.delete()#delete the user

    manager.delete()#delete the manager instance



    return redirect('manager_list')

def manager_group(request):

    group=Group.objects.all()

    return render(request,'back/manager/manager_group.html',{'group':group})

def manager_group_add(request):

    if request.method=="POST":
        name=request.POST.get('name')
        if  name!="":
            if len(Group.objects.filter(name=name))==0:
                group=Group(name=name)
                group.save()




    return redirect('manager_group')

def manager_group_del(request,name):

    b=Group.objects.filter(name=name)
    b.delete()

    return redirect('manager_group')

def user_groups(request,pk):

    manager=Manager.objects.get(pk=pk)
    print(manager.utxt)
    user=User.objects.get(username=manager.utxt)

    ugroup = []
    for i in user.groups.all():
        print(i.name)
        ugroup.append(i.name)

    group=Group.objects.all()

    return render(request,'back/manager/user_groups.html',{'ugroup':ugroup,'group':group})


def add_user_to_groups(request,pk):

    if request.method=="POST":

        gname=request.POST.get('gname')
        group=Group.objects.get(name=gname)
        manager=Manager.objects.get(pk=pk)
        user=User.objects.get(username=manager.utxt)
        user.groups.add(group)

    return redirect('user_groups',{pk:pk})

    #return render(request,'back/manager/user_groups.html')