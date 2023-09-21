from django.urls import path, include
from rest_framework import routers
#views
from .views import ListOwnersAPIView, RetrieveOwnersAPIView, CreateOwnersAPIView, UpdateOwnersAPIView, DeleteOwnersAPIView
#router

urlpatterns=[
    path("owners/", ListOwnersAPIView.as_view(), name="owners_list"),
    path("owners/<int:pk>/", RetrieveOwnersAPIView.as_view(), name="owners_detail"),
    path("owners/create/", CreateOwnersAPIView.as_view(), name="owners_create"),
    path("owners/<int:pk>/update", UpdateOwnersAPIView.as_view(), name="owners_update"),
    path("owners/<int:pk>/delete", DeleteOwnersAPIView.as_view(), name="owners_delete"),
]
