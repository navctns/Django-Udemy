from django.shortcuts import render
from .forms import DictionaryForm
# Create your views here.


def show_home(request):
    """Show the home page for searching domain"""
    search_result = {}

    if 'word' in request.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            search_result = form.search()

    else:
        form = DictionaryForm()
    return render(request, 'home_page.html',
                  {'form': form, 'search_result': search_result})