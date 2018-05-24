from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category   

class SubCategory(models.Model):
    subCategory = models.CharField(max_length=100)
    category = models.ForeignKey('Category', related_name = 'subCategories', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.subCategory   