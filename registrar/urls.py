from django.contrib import admin
from django.urls import path, include

from .views import RegistrarView, RegistrarSuspendView



urlpatterns = [
    #Registrar view
    path("list-registrar", RegistrarView.as_view(), name = "RegistrarView"),  
    path("edit-registrar/<id>", RegistrarView.as_view(), name = "RegistrarView"),  
    path("delete-registrar/<id>", RegistrarView.as_view(), name = "RegistrarView"),  
    path("create-registrar", RegistrarView.as_view(), name = "RegistrarView"),
    path("suspend-registrar/<id>", RegistrarSuspendView.as_view(), name = "RegistrarSuspendView"),  

]