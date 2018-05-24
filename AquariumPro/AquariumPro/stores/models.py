from django.db import models

# Create your models here.
class Store(models.Model):

    user_id = models.OneToOneField('userManagers.User', on_delete = models.CASCADE)
    name = models.CharField(max_length=20)
    shipping = models.ManyToManyField('shippings.Shipping')
    
    def __str__(self):
        return self.name