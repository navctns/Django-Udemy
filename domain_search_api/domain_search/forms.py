from django import forms
from django.conf import settings
import requests


class DictionaryForm(forms.Form):
    word = forms.CharField(max_length=100)

    def search(self):

        url = "https://domainr.p.rapidapi.com/v2/search"

        querystring = {"mashape-key": "undefined", "query": "acme cafe", "location": "de", "registrar": "dnsimple.com",
                       "defaults": "club,coffee"}

        headers = {
            'x-rapidapi-key': settings.X_RAPID_API_KEY,
            'x-rapidapi-host': "domainr.p.rapidapi.com",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)
