from django.contrib import admin
from django.urls import path, include

from .views import AssociationListView,NotificationEditFormView,AssociationEditFormView,CourtEditFormView,CourtListView, SuspendAssociationView,EditCourtView,MembershipPlanView,EditAssociationView,ToggleMembershipFineAmountView,ToggleMembershipPlanView, MembershipPaymentView,DeleteAssociationAdmin,DeleteAssociationView, NotificationView,ListNormalAdminView, CreateAssociationAdminView, DeleteAssociationView, CreateCourtView


urlpatterns = [
    
#court
   path("court/list", CourtListView.as_view(), name = "CourtListView"),
   path("court/create-court", CreateCourtView.as_view(), name = "CreateCourtView"),
   path("court/edit-court/<id>", EditCourtView.as_view(), name = "EditCourtView"),
   path("court/delete-court/<id>", CourtListView.as_view(), name = "CourtListView"),
   path("court/editform-court/<id>", CourtEditFormView.as_view(), name = "CourtEditFormView"),


#association
   path("list", AssociationListView.as_view(), name = "AssociationListView"),
   path("create-association", AssociationListView.as_view(), name = "AssociationListView"),
   path("edit-association/<id>", EditAssociationView.as_view(), name = "EditAssociationView"),
   path('delete-association/<id>',DeleteAssociationView.as_view(),name="DeleteAssociationView"),
   path("editform-association/<id>",AssociationEditFormView.as_view() ,name="AssociationEditFormView"),
   path("suspend-association/<id>", SuspendAssociationView.as_view(), name = "SuspendAssociationView"),
   path("delete-association-super-admin/<id>",DeleteAssociationAdmin.as_view() ,name="DeleteAssociationView"),
   path("delete-association-normal-admin/<id>",DeleteAssociationAdmin.as_view() ,name="DeleteAssociationAdmin"),
   path("association-normal-admin/list/<advocate_id>/<association_id>",ListNormalAdminView.as_view() ,name="ListNormalAdminView"),
   path("create-association-super-admin/<advocate_id>/<association_id>",CreateAssociationAdminView.as_view() ,name="CreateAssociationAdminView"),
   path("create-association-normal-admin/<advocate_id>/<association_id>",CreateAssociationAdminView.as_view() ,name="CreateAssociationAdminView"),

#membership plan
   path("membership-plan/list",MembershipPlanView.as_view(),name="MembershipPlanViews"),
   path("membership-plan/create",MembershipPlanView.as_view(),name="MembershipPlanView"),
   path("membership-plan/edit/<id>",ToggleMembershipPlanView.as_view(),name="ToggleMembershipPlanView"),
   path("membership-plan/delete/<id>",ToggleMembershipPlanView.as_view(),name="ToggleMembershipPlanView"),
   path("membership-plan/editform/<id>",ToggleMembershipPlanView.as_view(),name="ToggleMembershipPlanView"),


#membership fine amount
   path("fine-amount/create",ToggleMembershipFineAmountView.as_view(),name="ToggleMembershipFineAmountView"),
   path("fine-amount/edit/<id>",ToggleMembershipFineAmountView.as_view(),name="ToggleMembershipFineAmountView"),
   path("fine-amount/delete/<id>",ToggleMembershipFineAmountView.as_view(),name="ToggleMembershipFineAmountView"),
   path("fine-amount/list",ToggleMembershipFineAmountView.as_view(),name="ToggleMembershipFineAmountView"),   #not in api

#payment
   path("membership-payment/create",MembershipPaymentView.as_view() ,name="MembershipPaymentView"),
   path("membership-payment/list",MembershipPaymentView.as_view() ,name="MembershipPaymentView"),

 #notification
   path("notification/list",NotificationView.as_view() ,name="NotificationView"),
   path("notification/edit/<id>",NotificationView.as_view() ,name="NotificationView"),
   path("notification/create/<id>",NotificationView.as_view() ,name="NotificationView"),
   path("editform-notification/<id>",NotificationEditFormView.as_view() ,name="NotificationEditFormView"),
 
]