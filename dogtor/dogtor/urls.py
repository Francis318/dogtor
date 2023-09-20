"""
URL configuration for dogtor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.admin import blog_admin_site
from vet.admin import pet_admin_site



urlpatterns = [
    path('admin/', admin.site.urls),#panel por defecto
    path('blogadmin/', blog_admin_site.urls),#panel de blog de admin
    path('petadmin/', pet_admin_site.urls),#panel de blog de admin
    path("vet/", include(("vet.urls", "vet"))),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/",include(("api.urls","api"))),
]

#customizar panel de administrador
admin.site.index_title="Dogtor"
admin.site.site_header="Dogtor Admin"
admin.site.site_title="Dogtor Admin Panel"
