from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Snack

class Snacks(ListView):
    template_name='Home.html'
    model= Snack

class SnackList(DetailView):
    template_name='snack_detail.html'
    model= Snack
