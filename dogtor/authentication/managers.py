from django.contrib.auth.models import BaseUserManager

class ModUserManager(BaseUserManager):
    """Mod User Custom Manager."""
    #1. create user
    def create_user(self,email,user_name,first_name,password,**other_fields):
        """Overridign create_user func for ModUserManager"""
        #Agregar validaciones
        if not email:
            raise ValueError("You must provide an email.")
        email=self.normalize_email(email)

        #Nos hizo el usuario en la variable 'user'
        user=self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)

        #seteamos password
        user.set_password(password)

        #guardar en base de datos
        user.save()
        return user
    def create_superuser(self,email,user_name,first_name,password,**other_fields):
        """Overridign create_superuser func for ModUserManager"""
        #is_staff=verdadero
        #is_active=verdadero
        #is_superuser=verdadero
        other_fields.setdefault("is_staff",True)
        other_fields.setdefault("is_active",True)
        other_fields.setdefault("is_superuser",True)
        #Creamos el usuario con la funcion create_user
        return self.create_user(email, user_name, first_name, password, **other_fields)
    
    #2. create superuser
