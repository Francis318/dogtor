from django.shortcuts import render
from rest_framework import viewsets
from vet.models import PetOwner, Pet, PetDate
from .serializers import OwnersSerializers, PetsSerializers, PetDatesSerializers

# Create your views here.
class OwnersViewSet(viewsets.ModelViewSet):
    """ViewSet del modelo PetOwner"""
    #1. queryset que se va realizar (orm)
    #2. el serializador
    queryset=PetOwner.objects.all()
    serializer_class=OwnersSerializers

class PetsViewSet(viewsets.ModelViewSet):
    """ViewSet del modelo Pet"""
    #1. queryset que se va realizar (orm)
    #2. el serializador
    queryset=Pet.objects.all()
    serializer_class=PetsSerializers

class PetDatesViewSet(viewsets.ModelViewSet):
    """ViewSet del modelo PetDate"""
    #1. queryset que se va realizar (orm)
    #2. el serializador
    queryset=PetDate.objects.all()
    serializer_class=PetDatesSerializers
