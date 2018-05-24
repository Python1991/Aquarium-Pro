from django.db import models

# Create your models here.
class Evaluation(models.Model):
    comment = models.TextField()
    score = models.IntegerField()

    class Meta:
        abstract = True

class StoreEveluation(Evaluation):
    evaluation = models.ForeignKey('stores.Store', related_name = 'store_eveluations', on_delete = models.CASCADE)

    def __str__(self):
        return str(self.evaluation)

class PAPPEveluation(Evaluation):
    evaluation = models.ForeignKey('productAquaticPlantPackages.ProductAquaticPlantPackage', related_name = 'PAPP_eveluations', on_delete = models.CASCADE)

    def __str__(self):
        return str(self.evaluation)