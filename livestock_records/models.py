from django.db import models

# Create your models here.
class Species(models.Model):
    species_name = models.CharField(max_length=30)


class Animal(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    tag = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    color = models.ForeignKey(Color)
    dam = models.ForeignKey(self)
    sire = models.ForeignKey(self)
    

class NoteReason(models.Model):
    reason = models.CharField(max_length=30)

class Note(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateField()
