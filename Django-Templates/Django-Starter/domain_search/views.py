from django.shortcuts import render

# Create your views here.


def show_home(request):
    """Show the home page for searching domain"""

    return render(request, 'home_page.html')