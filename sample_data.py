"""
(petplannerpro) PS C:\development\python\petplannerpro> py  .\manage.py shell
Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from sample_data import build
>>> build()
>>> exit()
"""

from pets.models import Species, SizeClass, Breed, Pet

def build():

    spec1 = Species(name='Dog',description='Mans best friend')
    spec1.save()
    size1 = SizeClass(name='MediumDog',description='not too big',min_height_cm = 20,max_height_cm=100,min_weight_kg=10,max_weight_kg=25)
    size1.save()
    breed1 = Breed(name='Setter',description='zoomeyboi',breed_size=size1)
    breed1.save()
    pet1 = Pet(name='Oliver',breed=breed1,species=spec1)
    pet1.save()


    size2 = SizeClass(name='SmallDog',description='not big',min_height_cm = 10,max_height_cm=30,min_weight_kg=2,max_weight_kg=10)
    size2.save()

    breed2 = Breed(name='Pomeranian',description='hungryboi',breed_size=size1)
    breed2.save()
    pet2 = Pet(name='Koda',breed=breed2,species=spec1)
    pet2.save()


    breed3 = Breed(name='Maltise',description='grumpygurl',breed_size=size1)
    breed3.save()
    pet3 = Pet(name='Lady',breed=breed3,species=spec1)
    pet3.save()

