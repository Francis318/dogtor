from django.urls import path
#views
from .views import list_pet_owners, Test, OwnersList, OwnerDetail

urlpatterns=[
    path("owners/", OwnersList.as_view()),
    path("test/", Test.as_view()),
    path("owners/<int:pk>", OwnerDetail.as_view()),
]
