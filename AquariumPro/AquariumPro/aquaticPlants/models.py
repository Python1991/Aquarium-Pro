from django.db import models

# Create your models here.
class AquaticPlant(models.Model):
    name = models.CharField(max_length=100)
    unit = models.ForeignKey('units.Unit', related_name = '+', on_delete = models.CASCADE)
    degree_of_difficulty = models.IntegerField()
    selling_volume = models.IntegerField()
    image = models.ManyToManyField('images.Image')
    landscape_position = models.ManyToManyField('LandscapePosition')
    general_classification = models.ForeignKey('GeneralClassification', related_name = '+', on_delete = models.CASCADE)

    def __str__(self):
        return self.name    

class LandscapePosition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GeneralClassification(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name