# Generated by Django 2.0.4 on 2018-05-02 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productAquaticPlantPackages', '0002_productaquaticplant_product_aquatic_plant_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productaquaticplant',
            name='product_aquatic_plant_package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productAquaticPlants', to='productAquaticPlantPackages.ProductAquaticPlantPackage'),
        ),
    ]
