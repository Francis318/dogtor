from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

#Managers
from .managers import ModUserManager

class ModUser(AbstractBaseUser,PermissionsMixin):
    """Custom Moderator User"""
    #sobreescribir propiedades del modelo user
    #Extender (nuevos fields)
    email=models.EmailField(unique=True)
    user_name=models.CharField(max_length=150, unique=True)
    first_name=models.CharField(max_length=200, blank=True)
    start_date=models.DateTimeField(auto_now_add=True)
    about=models.TextField(max_length=500)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)

    #Manager del modelo
    objects=ModUserManager()

    #Campo identificador del user
    USERNAME_FIELD="email"

    #campos requeridos para cuando usamos el comando createsuperuser
    REQUIRED_FIELDS=["user_name","first_name"]
    #metodo string
    def __str__(self):
        return f"{self.user_name} {self.email}"