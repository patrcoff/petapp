from django.contrib import admin

# Register your models here.
from .models import Dosage, Frequency, Medecine, MedecineAssignment

admin.site.register(Dosage)
admin.site.register(Medecine)
admin.site.register(Frequency)
admin.site.register(MedecineAssignment)