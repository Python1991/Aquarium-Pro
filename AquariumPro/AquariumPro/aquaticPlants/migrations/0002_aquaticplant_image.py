# Generated by Django 2.0.4 on 2018-05-01 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('aquaticPlants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aquaticplant',
            name='image',
            field=models.ManyToManyField(to='images.Image'),
        ),
    ]
