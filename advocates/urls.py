from django.contrib import admin
from django.urls import path, include

from .views import AdvocatesListView, AdvocateEditFormView,SuspendAdvocateView, EditAdvocateProfileView

urlpatterns = [
   path("list", AdvocatesListView.as_view(), name = "AdvocatesListView"),
   path("create-advocate/", AdvocatesListView.as_view(), name = "AdvocatesListView"),
   path("suspend-advocate/<id>", SuspendAdvocateView.as_view(), name = "SuspendAssociationView"),
   path("edit-advocate/<id>", EditAdvocateProfileView.as_view(), name = "EditAdvocateProfileView"),
   path("editform-advocate/<id>", AdvocateEditFormView.as_view(), name = "AdvocateEditFormView"),


]