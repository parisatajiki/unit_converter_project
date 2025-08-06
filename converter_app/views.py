from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Quantity

class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data()
        context['quantitis'] = Quantity.objects.all()
        return context
