from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt# i think:when connecting to other websites(like payment gateway)

# Create your views here.
@csrf_exempt
def home(request):

    return render(request, 'front/home-page.html')