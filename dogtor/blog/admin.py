from django.contrib import admin

# Register your models here.

#panel de administracion para la app de blog
class BlogAdminArea(admin.AdminSite):
    """Blog admin panel administration"""
    site_header="Blog Site Admin Area"

#instanciarla nuestra clase para poder utilizarla
blog_admin_site=BlogAdminArea(name="BlogAdmin")