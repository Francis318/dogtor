from django.urls import path
#views
from .views import list_pet_owners, Test, OwnersList, OwnerDetail, PetsList, PetGet, OwnersCreate, OwnersUpdate, PetsCreate, PetsUpdate

urlpatterns=[
    path("owners/", OwnersList.as_view(), name="owners_list"),
    path("test/", Test.as_view()),
    path("owners/<int:pk>", OwnerDetail.as_view(), name="owners_detail"),
    path("pets/", PetsList.as_view(), name="pets_list"),
    path("pets/<int:pk>", PetGet.as_view(), name="pets_detail"),
    path("owners/add/", OwnersCreate.as_view(), name="owners_create"),
    path("owners/<int:pk>/edit/", OwnersUpdate.as_view(), name="owners_edit"),
    path("pets/add/", PetsCreate.as_view(), name="pets_create"),
    path("pets/<int:pk>/edit/", PetsUpdate.as_view(), name="pets_edit"),
]
