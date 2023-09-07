from django.contrib import admin
from django.urls import path, include

from .views import LawFirmListView,LawfirmEditFormView, SuspendLawFirmView,EditLawfirmView, DeletelawFirmView


urlpatterns = [
   path("list", LawFirmListView.as_view(), name = "LawFirmListView"),
   path("suspend-lawfirm/<id>", SuspendLawFirmView.as_view(),  name= "SuspendLawFirmView"),
   path("delete-lawfirm/<id>", DeletelawFirmView.as_view(),  name= "DeletelawFirmView"),
   path("edit-lawfirm/<id>", EditLawfirmView.as_view(),  name= "EditLawfirmView"),
   path("editform-lawfirm/<id>", LawfirmEditFormView.as_view(),  name= "LawfirmEditFormView"),



   path("create-lawfirm/", LawFirmListView.as_view(), name = "LawFirmListView"),   #not in api

]