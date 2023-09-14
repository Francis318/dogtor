from django.contrib import admin

# Register your models here.

from .models import PetOwner, Pet, PetDate

#panel de administracion para la app de blog
class PetAdminArea(admin.AdminSite):
    """Pet admin panel administration"""
    site_header="Pet Site Admin Area"

#instanciarla nuestra clase para poder utilizarla
pet_admin_site=PetAdminArea(name="PetAdmin")

#registramos modelo 'Post' en nuestro admin area
pet_admin_site.register(PetOwner)
pet_admin_site.register(Pet)
pet_admin_site.register(PetDate)

#Registrarlo en el admin area general de admin
admin.site.register(PetOwner)
admin.site.register(Pet)
admin.site.register(PetDate)