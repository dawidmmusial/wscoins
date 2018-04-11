import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wscoins.settings')
app = Celery('wscoins')
app.config_from_object('django.conf:settings', namespace='CELERY')
# Searching tasks.py in modules
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)