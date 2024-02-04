from django.urls import path
from .views import *
urlpatterns=[
    path("",regform,name="regform"),
    path("delete/<int:id>/",delete,name="delete"),
    path("edit/<int:id>/",edit,name="edit")
]