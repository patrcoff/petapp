from django.db import models
from django.conf import settings
from pets.models import Pet
# Create your models here.

class Dosage(models.Model):
    """Description of dosage unit type i.e. 1 pill, 1mm etc"""

    name = models.CharField(max_length=20)
    unit = models.CharField(max_length=5)#cm, mm, each, 
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Frequency(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Medecine(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    dosage_type = models.ForeignKey(Dosage, on_delete=models.CASCADE)
    dosage_size = models.IntegerField(verbose_name="Per unit Dosage in mg of main active ingredient.")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,    
                                    verbose_name="Created by", 
                                    related_name="medecine",  
                                    on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
        
class MedecineAssignment(models.Model):
    """Instance of an assignment of a dose of a medecine to a specific pet"""
    
    friendly_name = models.CharField(max_length=25)
    medecine = models.ForeignKey(Medecine, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    dosage = models.IntegerField(verbose_name="Number of doses per application",default=1)
    frequency = models.ForeignKey(Frequency, on_delete=models.CASCADE)
    vetenary_guidance = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.pet} : {self.medecine}'