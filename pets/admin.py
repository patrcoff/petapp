from django.contrib import admin

# Register your models here.
from .models import Species, Breed, SizeClass

admin.site.register(Species)
admin.site.register(Breed)
admin.site.register(SizeClass)
