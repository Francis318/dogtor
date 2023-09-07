from typing import Any
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View, TemplateView
# Create your views here.
from vet.models import PetOwner
def list_pet_owners(request):
    owners=PetOwner.objects.all()
    context={"owners": owners}
    template=loader.get_template("vet/owners/list.html")
    return HttpResponse(template.render(context, request))

class OwnersList(TemplateView):
    #reenderizar el template
    template_name="vet/owners/list.html"
    #contexto del template
    def get_context_data(self, **kwargs):
        #agarrar el contexto de TemplateView
        context=super().get_context_data(**kwargs)
        #le agregamos nuestro custom context
        context["owners"]=PetOwner.objects.all()
        return context


class Test(View):
    #como funcion el metodo(GET,PATCH,POST,DELETE,PUT)
    def get(self, request):
        return HttpResponse("Hello world from a class generic view")