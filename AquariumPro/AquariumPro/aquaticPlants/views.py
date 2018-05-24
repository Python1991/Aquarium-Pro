from django.shortcuts import render
from .models import AquaticPlant
# Create your views here.
def landscape_position(request, landscape_position):
    a = AquaticPlant.objects.filter(landscape_position__name = landscape_position)
    return render(request, 'pages/index.html', {'Products':a})

def general_classification(request, general_classification):
    a = AquaticPlant.objects.filter(general_classification__name = general_classification)
    return render(request, 'pages/index.html', {'Products':a})