# medecine/urls.py

from django.urls import path
#from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path(
        "assign",
        views.MedecineAssignmentCreateView.as_view(),
        name="assign-meds"
    ),
]