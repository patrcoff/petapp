#from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (

    ListView,
    CreateView,
)

# Create your views here.
from medecines.models import Medecine, MedecineAssignment

class MedecineAssignmentCreateView(CreateView):
    model = MedecineAssignment
    fields = ['friendly_name', 'medecine', 'pet', 'dosage', 'frequency', 'vetenary_guidance']
    success_url = reverse_lazy("assign-meds")