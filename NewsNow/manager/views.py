from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User,Group,Permission
from django.contrib.contenttypes.models import ContentType



from .models import Manager
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from trending.models import Trending

def manager_list(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end
    # check for permission
    perm = 0
    for i in request.user.groups.all():

        if i.name == "masteruser":
            perm = 1
    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    # end check for permission


    manager=Manager.objects.all()

    return render(request,'back/manager/manager_list.html',{'manager':manager})

def manager_del(request,pk):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end
    # check for permission
    perm = 0
    for i in request.user.groups.all():

        if i.name == "masteruser":
            perm = 1
    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    # end check for permission

    manager=Manager.objects.get(pk=pk)
    b=User.objects.filter(username=manager.utxt)
    b.delete()#delete the user

    manager.delete()#delete the manager instance



    return redirect('manager_list')

def manager_group(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    perm=0
    for i in request.user.groups.all():

        if i.name =="masteruser":
            perm=1
    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})

    group=Group.objects.all().exclude(name='masteruser')

    return render(request,'back/manager/manager_group.html',{'group':group})

def manager_group_add(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end
    #check for permission
    perm = 0
    for i in request.user.groups.all():

        if i.name == "masteruser":
            perm = 1
    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    #end check for permission
    if request.method=="POST":
        name=request.POST.get('name')
        if  name!="":
            if len(Group.objects.filter(name=name))==0:
                group=Group(name=name)
                group.save()




    return redirect('manager_group')

def manager_group_del(request,name):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    b=Group.objects.filter(name=name)
    b.delete()

    return redirect('manager_group')

def user_groups(request,pk):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    # check for permission
    perm = 0
    for i in request.user.groups.all():

        if i.name == "masteruser":
            perm = 1
    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    # end check for permission

    manager=Manager.objects.get(pk=pk)
    print(manager.utxt)
    user=User.objects.get(username=manager.utxt)

    ugroup = []
    for i in user.groups.all():
        print(i.name)
        ugroup.append(i.name)

    group=Group.objects.all()

    return render(request,'back/manager/user_groups.html',{'ugroup':ugroup,'group':group,'pk':pk})


def add_user_to_groups(request,pk):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    if request.method=="POST":

        gname=request.POST.get('gname')
        group=Group.objects.get(name=gname)
        manager=Manager.objects.get(pk=pk)
        user=User.objects.get(username=manager.utxt)
        user.groups.add(group)

    return redirect('user_groups',pk=pk)

    #return render(request,'back/manager/user_groups.html')

def del_user_from_groups(request,pk,name):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    group=Group.objects.get(name=name)#getting the group with the name
    manager=Manager.objects.get(pk=pk)#get manager corresponding with pk
    user=User.objects.get(username=manager.utxt)#get user with username=manager.utxt
    user.groups.remove(group) #remove group

    return redirect('user_groups',pk=pk)

def manager_perms(request):

    #for managing all permissions
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    perm=0
    for i in request.user.groups.all():

        if i.name =="masteruser":
            perm=1
    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})

    perms=Permission.objects.all()

    return render(request,'back/manager/manager_perms.html',{'perms':perms})

def manager_perms_del(request,name):

    #delete permissions
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    perms=Permission.objects.filter(name=name)
    perms.delete()

    return redirect('manager_perms')

def manager_perms_add(request):

    #delete permissions
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    if request.method =="POST":

        name=request.POST.get('name')
        cname=request.POST.get('cname')
        print(name)

        #creating permission

        if len(Permission.objects.filter(codename=cname))==0:
            content_type=ContentType.objects.get(app_label="main",model="main")
            permission=Permission.objects.create(codename=cname,name=name,content_type=content_type)
        else:
            error = "This codename alrady Exists"
            return render(request, 'back/error.html', {'error': error})




    return redirect('manager_perms')


def user_perms(request,pk):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    # check for permission
    perm = 0
    for i in request.user.groups.all():

        if i.name == "masteruser":
            perm = 1
    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    # end check for permission

    manager=Manager.objects.get(pk=pk)
    print(manager.utxt)
    user=User.objects.get(username=manager.utxt)
    permission=Permission.objects.filter(user=user)

    uperms = []
    for i in permission:
        print(i.name)
        uperms.append(i.name)

    perms=Permission.objects.all()

    return render(request,'back/manager/user_perms.html',{'uperms':uperms,'pk':pk,'perms':perms})


def user_perms_del(request,pk,name):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    # check for permission
    perm = 0
    for i in request.user.groups.all():

        if i.name == "masteruser":
            perm = 1
    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    # end check for permission

    manager=Manager.objects.get(pk=pk)
    print(manager.utxt)
    user=User.objects.get(username=manager.utxt)
    permission=Permission.objects.get(name=name)
    user.user_permissions.remove(permission)
    return redirect('user_perms',pk=pk)

def user_perms_add(request,name):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    # check for permission
    perm = 0
    for i in request.user.groups.all():

        if i.name == "masteruser":
            perm = 1
    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    # end check for permission

    if request.method == 'POST':

        pname=request.POST.get('pname')

        manager=Manager.objects.get(pk=pk)
        print(manager.utxt)
        user=User.objects.get(username=manager.utxt)

        permission=Permission.objects.get(name=pname)
        user.user_permissions.add(permission)

        return redirect('user_perms',pk=pk)


def groups_perms(request,name):
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    # check for permission
    perm = 0
    for i in request.user.groups.all():

        if i.name == "masteruser":
            perm = 1
    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    # end check for permission


    group=Group.objects.get(name=name)
    perms=group.permissions.all()
    allperms=Permission.objects.all()


    return render(request,'back/manager/groups_perms.html',{'perms':perms,'name':name,'allperms':allperms})

def groups_perms_del(request,gname,name):

    #gname is for the group, name is for the permission name
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    # check for permission
    perm = 0
    for i in request.user.groups.all():

        if i.name == "masteruser":
            perm = 1
    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    # end check for permission

    group=Group.objects.get(name=gname)
    perm=Permission.objects.get(name=name)
    group.permissions.remove(perm)

    return redirect('groups_perms',name=gname)

def groups_perms_del(request,gname,name):

    #gname is for the group, name is for the permission name
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    # check for permission
    perm = 0
    for i in request.user.groups.all():

        if i.name == "masteruser":
            perm = 1
    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    # end check for permission

    group=Group.objects.get(name=gname)
    perm=Permission.objects.get(name=name)
    group.permissions.remove(perm)

    return redirect('groups_perms',name=gname)

def groups_perms_add(request,name):

    #gname is for the group, name is for the permission name
    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    # check for permission
    perm = 0
    for i in request.user.groups.all():

        if i.name == "masteruser":
            perm = 1
    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    # end check for permission
    if request.method == "POST":

        pname=request.POST.get('pname')
        group=Group.objects.get(name=name)
        perm=Permission.objects.get(name=pname)
        group.permissions.add(perm)

    return redirect('groups_perms',name=name)










