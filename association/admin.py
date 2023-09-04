from .models import Court,Jurisdiction,Association,AssociationMembershipPayment,AssociationPaymentRequest, Notification,MembershipFineAmount,MembershipPlan
from django.contrib import admin

# Register your models here.

admin.site.register(Court)
admin.site.register(Jurisdiction)
admin.site.register(Association)
admin.site.register(AssociationMembershipPayment)
admin.site.register(AssociationPaymentRequest)
admin.site.register(Notification)
admin.site.register(MembershipFineAmount)
admin.site.register(MembershipPlan)

