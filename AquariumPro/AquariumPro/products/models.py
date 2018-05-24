from django.db import models
# Create your models here.
class Product(models.Model):

    store = models.ForeignKey('stores.Store', related_name='products', on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name