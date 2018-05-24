from django.shortcuts import render
from .models import ProductAquaticPlant ,ProductAquaticPlantPackage
# Create your views here.
def aquatic_plant(request, aquatic_plant_id):
    paps = ProductAquaticPlant.objects.filter(aquatic_plant = aquatic_plant_id)
    papp = list()
    for pap in paps:
        pap.product_aquatic_plant_package.images = pap.images()
        papp.append(pap.product_aquatic_plant_package)

    return render(request, 'pages/Products/products.html', {'Products':papp})


def product_aquatic_plant_package(request, product_aquatic_plant_package_id):
    product_aquatic_plant_package = ProductAquaticPlantPackage.objects.filter(id = product_aquatic_plant_package_id).get()
    images = list()
    for pap in product_aquatic_plant_package.productAquaticPlants.all():
        for image in pap.image.all():
            images.append(image)
    product_aquatic_plant_package.images = images
    # store = product_aquatic_plant_package.store.shipping.all
    # assert False
    return render(request, 'pages/Products/product_aquatic_plant_package.html', {'product_aquatic_plant_package':product_aquatic_plant_package})    