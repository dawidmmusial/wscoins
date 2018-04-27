from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .tools import get_cryptocurrency

class MonitorView(TemplateView):
    template_name = 'monitor.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cryptocurrency'] = get_cryptocurrency(settings.CRYPTOCOMPARE_API_PRICES)
        return context