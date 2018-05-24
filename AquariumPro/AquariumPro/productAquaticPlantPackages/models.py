from django.db import models
from products.models import Product
# Create your models here.
class ProductAquaticPlantPackage(Product):
    unit = models.ForeignKey('units.Unit', related_name = '+', on_delete = models.CASCADE)
    category = models.ForeignKey('categories.Category', related_name = '+', on_delete = models.CASCADE)


    class Meta:
        verbose_name = '產品-水草包'
        verbose_name_plural = '產品-水草包'



class ProductAquaticPlant(models.Model):
    aquatic_plant = models.ForeignKey('aquaticPlants.AquaticPlant', related_name = 'productAquaticPlants', on_delete = models.CASCADE)
    product_aquatic_plant_package = models.ForeignKey('ProductAquaticPlantPackage', related_name = 'productAquaticPlants', on_delete = models.CASCADE)
    image = models.ManyToManyField('images.Image')
    algae_level = models.IntegerField()
    gastropoda_level = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        verbose_name = '產品-水草'
        verbose_name_plural = '產品-水草'

    def __str__(self):
        return self.aquatic_plant.name

    def images(self):
        return self.image.all()