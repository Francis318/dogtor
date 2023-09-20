from rest_framework import serializers
from vet.models import PetOwner, Pet

class OwnersSerializers(serializers.HyperlinkedModelSerializer):
    """Pet owners serializer"""
    class Meta:
        model=PetOwner
        fields=["id", "first_name", "last_name", "email", "address", "phone", "created_at"]
    

class PetsSerializers(serializers.HyperlinkedModelSerializer):
    """Pets serializer"""
    class Meta:
        model=Pet
        fields=["id", "name", "type", "owner"]