from rest_framework import serializers
from userapp.models import Advocate

class RegistrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data.get('type_of_user') == 'registrar':
            return data
        return None
