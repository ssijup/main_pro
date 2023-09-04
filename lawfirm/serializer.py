from rest_framework import serializers

from .models import LawFirm


class LawFirmListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawFirm
        fields = "__all__"