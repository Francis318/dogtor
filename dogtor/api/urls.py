from django.urls import path, include
from rest_framework import routers
#views
from .views import ListCreateOwnersAPIView, UpdateDestroyOwnersAPIView
#router

urlpatterns=[
    path("owners/", ListCreateOwnersAPIView.as_view(), name="owners_list_create"),#crea y revisa
    path("owners/<int:pk>/", UpdateDestroyOwnersAPIView.as_view(), name="owners_update_delete"),
]
