from typing import Any
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
from vet.models import PetOwner, Pet
from .forms import OwnerForm, PetForm


def list_pet_owners(request):
    owners = PetOwner.objects.all()
    context = {"owners": owners}
    template = loader.get_template("vet/owners/list.html")
    return HttpResponse(template.render(context, request))


class OwnersList(ListView):
    # Modelo con el que estamos manipulando
    # El template
    # El contexto que va a tener el template
    model = PetOwner
    template_name = "vet/owners/list.html"
    context_object_name = "owners"


class OwnerDetail(LoginRequiredMixin, DetailView):
    """Render a specific Pet owner with their pk."""

    # Modelo con el que estamos manipulando
    # El template
    # El contexto que va a tener el template
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"


class PetsList(ListView):
    # Modelo con el que estamos manipulando
    # El template
    # El contexto que va a tener el template
    model = Pet
    template_name = "vet/pets/pet_list.html"
    context_object_name = "pets"


class PetGet(DetailView):
    """Render a specific Pet owner with their pk."""

    # Modelo con el que estamos manipulando
    # El template
    # El contexto que va a tener el template
    model = Pet
    template_name = "vet/pets/detail.html"
    context_object_name = "pet"


class OwnersCreate(CreateView):
    """View used to create PetOwner"""

    # 1.Modelo
    # 2.Template a renderizar
    # 3.El formulario con el que se va a crear
    # 4.La url a redireccionar si la request fue exitosa y va a ser una reverse
    model = PetOwner
    template_name = "vet/owners/create.html"
    form_class = OwnerForm
    # urls a donde se va a redireccionar si fue exitosa nuestra creacion
    success_url = reverse_lazy("vet:owners_list")

class OwnersUpdate(PermissionRequiredMixin, UpdateView):
    """View used to update a PetOwner"""
    #Permiso que necesita para entrar
    permission_required="vet.change_petowner"
    raise_exception=False
    login_url="/admin/login"
    redirect_field_name="next"

    model = PetOwner
    template_name = "vet/owners/update.html"
    form_class = OwnerForm
    # urls a donde se va a redireccionar si fue exitosa nuestra creacion
    success_url = reverse_lazy("vet:owners_list")

class PetsCreate(CreateView):
    """View used to create PetOwner"""

    # 1.Modelo
    # 2.Template a renderizar
    # 3.El formulario con el que se va a crear
    # 4.La url a redireccionar si la request fue exitosa y va a ser una reverse
    model = Pet
    template_name = "vet/pets/create.html"
    form_class = PetForm
    # urls a donde se va a redireccionar si fue exitosa nuestra creacion
    success_url = reverse_lazy("vet:pets_list")

class PetsUpdate(UpdateView):
    """View used to update a PetOwner"""
    model = Pet
    template_name = "vet/pets/update.html"
    form_class = PetForm
    # urls a donde se va a redireccionar si fue exitosa nuestra creacion
    success_url = reverse_lazy("vet:pets_list")

class Test(View):
    # como funcion el metodo(GET,PATCH,POST,DELETE,PUT)
    def get(self, request):
        return HttpResponse("Hello world from a class generic view")
