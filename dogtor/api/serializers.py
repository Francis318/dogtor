from rest_framework import serializers
from vet.models import PetOwner, Pet, PetDate

class OwnersSerializers(serializers.HyperlinkedModelSerializer):
    """Pet owners serializer"""
    class Meta:
        model=PetOwner
        fields=["id", "first_name", "last_name", "email", "address", "phone", "created_at"]
    

class PetsSerializers(serializers.HyperlinkedModelSerializer):
    """Pets serializer"""
    owner=serializers.PrimaryKeyRelatedField(queryset=PetOwner.objects.all(), many=False)
    class Meta:
        model=Pet
        fields=["id", "name", "type", "owner"]


class PetDatesSerializers(serializers.HyperlinkedModelSerializer):
    """PetDates serializer"""
    pet=serializers.PrimaryKeyRelatedField(queryset=Pet.objects.all(), many=False)
    class Meta:
        model=PetDate
        fields=["id", "datetime", "type", "pet"]

class OwnersListSerializer(serializers.ModelSerializer):
    """Serializer to list all Pet Owner"""
    class Meta:
        model=PetOwner
        fields=["id", "first_name", "last_name"]

class OwnersDetailSerializer(serializers.ModelSerializer):
    """Serializer to the Detail of a Pet Owner"""
    class Meta:
        model=PetOwner
        fields="__all__"

class OwnersCreateSerializer(serializers.ModelSerializer):
    """Serializer to create of a Pet Owner"""
    class Meta:
        model=PetOwner
        fields="__all__"

class OwnersUpdateSerializer(serializers.ModelSerializer):
    """Serializer to update of a Pet Owner"""
    class Meta:
        model=PetOwner
        fields="__all__"

class OwnersDeliteSerializer(serializers.ModelSerializer):
    """Serializer to update of a Pet Owner"""
    class Meta:
        model=PetOwner
        fields="__all__"
