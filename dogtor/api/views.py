from django.shortcuts import render
from rest_framework import viewsets, generics
from vet.models import PetOwner, Pet, PetDate
from .serializers import OwnersSerializers, PetsSerializers, PetDatesSerializers, OwnersListSerializer, OwnersDetailSerializer, OwnersCreateSerializer, OwnersUpdateSerializer, OwnersDeliteSerializer

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

class ListOwnersAPIView(generics.ListAPIView):
    """List Owners Api View."""
    queryset=PetOwner.objects.all().order_by("created_at")
    #serializador
    serializer_class=OwnersListSerializer

class RetrieveOwnersAPIView(generics.RetrieveAPIView):
    """Detail Pet Owner Api View"""
    queryset=PetOwner.objects.all()
    #serializador
    serializer_class=OwnersDetailSerializer

class CreateOwnersAPIView(generics.CreateAPIView):
    """Create Pet Owner Api View"""
    queryset=PetOwner.objects.all()
    #serializador
    serializer_class=OwnersCreateSerializer

class UpdateOwnersAPIView(generics.UpdateAPIView):
    """Update Pet Owner Api View"""
    queryset=PetOwner.objects.all()
    #serializador
    serializer_class=OwnersUpdateSerializer

class DeleteOwnersAPIView(generics.DestroyAPIView):
    """Update Pet Owner Api View"""
    queryset=PetOwner.objects.all()
    #serializador
    serializer_class=OwnersDeliteSerializer
    