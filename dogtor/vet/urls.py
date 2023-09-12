from django.urls import path
#views
from .views import list_pet_owners, Test, OwnersList, OwnerDetail, PetsList, PetGet

urlpatterns=[
    path("owners/", OwnersList.as_view(), name="owners_list"),
    path("test/", Test.as_view()),
    path("owners/<int:pk>", OwnerDetail.as_view(), name="owners_detail"),
    path("pets/", PetsList.as_view()),
    path("pets/<int:pk>", PetGet.as_view()),
]
