from django.db import models

# Create your models here.
class Shipping(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.category + ' ' + self.name