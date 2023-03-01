#from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (

    ListView,
    CreateView,
)

# Create your views here.

from .models import Pet


class PetListView(ListView):
    model = Pet
    queryset = Pet.objects.all().order_by("species")

class PetCreateView(CreateView):
    model = Pet
    fields = ['name','species','breed']
    success_url = reverse_lazy("pet-create")

