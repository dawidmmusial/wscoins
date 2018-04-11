import json
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from .tools import get_cryptocompare_prices

@shared_task
def test_send(val):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('mcoins', {'type': 'task.message','message': val})

@shared_task
def send_cryptocompare_prices():
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('mcoins', {'type': 'send.prices','data': get_cryptocompare_prices()})