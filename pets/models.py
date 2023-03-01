from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

# Create your models here.

class Species(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class SizeClass(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    min_height_cm = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    min_weight_kg = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    max_height_cm = models.IntegerField(validators=[MaxValueValidator(150), MinValueValidator(1)])
    max_weight_kg = models.IntegerField(validators=[MaxValueValidator(150), MinValueValidator(1)])
    
    def __str__(self):
        return self.name

class Breed(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    breed_size = models.ForeignKey(SizeClass, on_delete=models.CASCADE)
    #how do we handle same breed name of different species?
    #uniqueness of name+species_id (need to add fk to species for this)

    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=20)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,    
                                    verbose_name="Created by", 
                                    related_name="pets",  
                                    on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}: {self.breed}'


    #sizeclass is to be used to define expected sizes of breeds, separate from actual dog size
    #these expected sizes will be used in the app to determine if the individual pet is within expected range for its breed
    #each species will have its own size classes i.e. 'LargeDog' etc