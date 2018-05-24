"""credit_agency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from .views import landscape_position, general_classification

landscape_position_pattern = [
    path('<landscape_position>', landscape_position)
]
general_classification_pattern = [
    path('<general_classification>', general_classification)
]

urlpatterns = [
    path('landscape_position/', include(landscape_position_pattern)),
    path('general_classification/', include(general_classification_pattern)),
]
