import random
from django.shortcuts import render
from productAquaticPlantPackages.models import ProductAquaticPlantPackage
# Create your views here.
def index(request):
    papps = ProductAquaticPlantPackage.objects.all()
    for papp in papps:
        papp.img = random.choice(random.choice(papp.productAquaticPlants.all()).image.all()).url
    return render(request, 'pages/index.html', {'product_aquatic_plant_packages' : papps})

def category(request):
    return render(request, 'pages/index.html')