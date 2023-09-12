from typing import Any
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
# Create your views here.
from vet.models import PetOwner, Pet
def list_pet_owners(request):
    owners=PetOwner.objects.all()
    context={"owners": owners}
    template=loader.get_template("vet/owners/list.html")
    return HttpResponse(template.render(context, request))

class OwnersList(ListView):
    #Modelo con el que estamos manipulando
    #El template
    #El contexto que va a tener el template
    model=PetOwner
    template_name="vet/owners/list.html"
    context_object_name="owners"

class OwnerDetail(DetailView):
    """Render a specific Pet owner with their pk."""
    #Modelo con el que estamos manipulando
    #El template
    #El contexto que va a tener el template
    model=PetOwner
    template_name="vet/owners/detail.html"
    context_object_name="owner"

class PetsList(TemplateView):
    #reenderizar el template
    template_name="vet/pets/pet_list.html"
    #contexto del template
    def get_context_data(self, **kwargs):
        #agarrar el contexto de TemplateView
        context=super().get_context_data(**kwargs)
        #le agregamos nuestro custom context
        context["pets"]=Pet.objects.all()
        return context
    
class PetGet(TemplateView):
    #reenderizar el template
    template_name="vet/pets/detail.html"
    #contexto del template
    def get_context_data(self, **kwargs):
        #agarrar el contexto de TemplateView
        print("KWARGS",kwargs)
        context=super().get_context_data(**kwargs)
        #le agregamos nuestro custom context
        context["pet"]=Pet.objects.get(pk=kwargs["pk"])
        return context

class Test(View):
    #como funcion el metodo(GET,PATCH,POST,DELETE,PUT)
    def get(self, request):
        return HttpResponse("Hello world from a class generic view")