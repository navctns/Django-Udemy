from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

from .models import Cat
import csv
from django.http import HttpResponse

def cat_list(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    cat=Cat.objects.all()
    # cat_del = Cat.objects.filter(count = 0)#for deleting categories without news
    # cat_del.delete()
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
            return render(request,'back/error.html',{'error':error})
        b=Cat(name=name)
        b.save()
        return redirect('cat_list')

    return render(request,'back/cat_add.html')

def export_cat_csv(request):

    response = HttpResponse(content_type = 'text/csv' )
    response['content-Disposition'] = 'attachment; filename ="cat.csv"'#for creating a download file
    writer = csv.writer(response)
    writer.writerow(['Title','Counter'])
    for i in Cat.objects.all():
        writer.writerow([i.name, i.count])#write name and count to csv

    return response

def import_cat_csv(request):

    if request.method == 'POST':

        csv_file = request.FILES["csv_file"]
        #check file
        if not csv_file.name.endswith('.csv'):
            error = "Please Input csv file"
            return render(request, 'back/error.html', {'error': error})
        if csv_file.multiple_chunks():
            error = "File too Large"
            return render(request, 'back/error.html', {'error': error})
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\r")
        # lines = lines.split('\n')
        lines_1 = "".join(lines).split('\n')
        lines_2 = "".join(lines_1).split(',')
        # lines_3 =

        print(lines_1)
        print(lines)
        print("lines2",lines_2)
        fields = []
        for line in lines_1:
            print("lines",line)
            # fields.append(line.split(","))
            fields = fields + line.split(',')
        print("fields,type",fields, type(fields))
        fields1 = []
        for i in range(0,len(fields)-1,2):
            fields1.append((fields[i],fields[i+1]))#store name of category and count in tuples(a,b)
        try:
            # print(fields1[0], fields1[1])
            for new in fields1:
                if len(Cat.objects.filter(name = new[0])) == 0 and new[0] != "Title" and new[0] != "":
                    b = Cat(name = new[0])
                    b.save()
        except:
            print("finish")

    return redirect('cat_list')

