from django.db import models

# Create your models here.
class Image(models.Model):
    url = models.CharField(max_length=200)
    clicks = models.IntegerField()
    image_source = models.ForeignKey('ImageSource', related_name = '+', on_delete = models.CASCADE)

    def __str__(self):
        return self.url

class ImageSource(models.Model):
    source = models.CharField(max_length=100)

    def __str__(self):
        return self.source