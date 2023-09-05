from rest_framework import serializers

from .models import Association, Jurisdiction ,Court, MembershipPlan, MembershipFineAmount, Notification, AssociationMembershipPayment
# from userapp.models import AdminRole
# from association.models import ASSOCIATION_ROLE_TYPE_CHOICES



class CourtListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Court
        fields="__all__"

class AssociationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Association
        fields = "__all__"

# class CreateAssociationAdminSerializer(serializers.Serializer):
#     admin_roles = serializers.ChoiceField(choices=ASSOCIATION_ROLE_TYPE_CHOICES)

# class ListNormalAdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdminRole
#         fields = "__all__"

class MembershipPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipPlan
        fields = "__all__"

class MembershipFineAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipFineAmount
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields="__all__"


class AssociationMembershipPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=AssociationMembershipPayment
        fields="__all__"