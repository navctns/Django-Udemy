from django.shortcuts import render, HttpResponse
from PyPDF2 import PdfFileReader,PdfFileWriter# Create your views here.
from django.core.files.storage import FileSystemStorage
import mimetypes

def show_home(request):

    file_encript = '' #file Encripted or not
    if request.method == 'POST':

        try:
            fs=FileSystemStorage()
            myfile=request.FILES['myfile']# myfile from the name of the html input
            filename=fs.save(myfile.name,myfile)
            url1=fs.url(filename)
            print('Url1',url1)

            out = PdfFileWriter()
            file = PdfFileReader(myfile)
            print(file)

            # Get number of pages in original file
            num = file.numPages
            print('num',num)
            # Iterate through every page of the original
            # file and add it to our new file.
            for idx in range(num):
                # Get the page at index idx
                print('Loop',idx)
                page = file.getPage(idx)
                # add it to the output file
                out.addPage(page)

            print('Out',out)
            # Store Password
            password = '1245'

            # Encrypt new file with Password
            out.encrypt(password)

            # Open a new file "myfile_encrypted.pdf"

            with open('media/polynomial_encrypted.pdf', 'wb') as f:
                # Write our encrypted PDF to this file
                out.write(f)

            file_encript = '1'

        except:
            print('input file')


    return render(request,'encryption.html',{'file_encript':file_encript,'file_path':'media/polynomial_encrypted.pdf'})

# def encrypt_file(request):

def download_encripted_file(request):
    """ Generate Download link for the Encripted File"""

    fl_path = 'media/'
    file_name = 'polynomial_encripted.pdf'
    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % file_name

    return response