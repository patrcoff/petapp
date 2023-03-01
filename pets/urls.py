# pets/urls.py

from django.urls import path
#from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path(
        "",
        views.PetListView.as_view(),
        name="pet-list"
    ),
    path(
        "new",
        views.PetCreateView.as_view(),
        name="pet-create"
    ),

    
]
