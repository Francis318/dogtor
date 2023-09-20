from django.urls import path, include
from rest_framework import routers
#views
from .views import OwnersViewSet, PetsViewSet
#router
router=routers.DefaultRouter()
router.register(r"owners",OwnersViewSet)
router.register(r"pets",PetsViewSet)

urlpatterns=[
    path("",include(router.urls))
]