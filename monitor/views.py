from django.shortcuts import render
from django.views.generic.base import TemplateView

class MonitorView(TemplateView):
	template_name = 'monitor.html'
