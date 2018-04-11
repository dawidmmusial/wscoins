import json
from django.conf import settings
from urllib import request

def get_cryptocompare_prices():
    jurl = request.urlopen(settings.CRYPTOCOMPARE_API_PRICES)
    data = jurl.read().decode('utf-8')
    return data