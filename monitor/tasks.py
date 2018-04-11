from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from django.conf import settings
from wscoins.celery import app
from .tools import get_cryptocurrency

app.conf.beat_schedule = {
    'send-cryptocurency-value-every-10-seconds': {
        'task': 'monitor.tasks.send_cryptocompare_prices',
        'schedule': 10.0
    },
}

@shared_task
def send_cryptocompare_prices():
    """Task send to channel layer's group cryptocurrencys value"""
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('mcoins', {'type': 'send.prices','data': get_cryptocurrency(settings.CRYPTOCOMPARE_API_PRICES)})