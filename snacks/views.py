from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Snack

class Snacks(TemplateView):
    template_name='Home.html'

class SnackList(ListView):
    template_name='snack_detail.html'
    model= Snack
