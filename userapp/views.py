from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, UserOnlySerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import UserData, Advocate

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class IsNormalUser(IsAuthenticated):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.type_of_user == "normal_user"

class ExampleView(APIView):
    permission_classes = [IsNormalUser]
    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
    

from rest_framework import generics
from .models import UserData
from .serializers import UserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserSerializer

class UserOnlyCreateAPIView(generics.CreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserOnlySerializer