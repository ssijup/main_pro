# from rest_framework import serializers
# from userapp.models import Advocate


# class AdvocatesListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Advocate
#         fields = "__all__"


from rest_framework import serializers
from userapp.models import UserData, Advocate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['id', 'name', 'email', 'date_joined', 'is_admin', 'is_active', 'is_staff', 'is_superuser']

class AdvocatesListSerializer(serializers.ModelSerializer):
    user = UserSerializer() 
    class Meta:
        model = Advocate
        fields = '__all__'