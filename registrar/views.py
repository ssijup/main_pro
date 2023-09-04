from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django.shortcuts import render
from rest_framework import status

from userapp.models import Advocate
from .serializer import RegistrarSerializer


class RegistrarView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegistrarSerializer(data = data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({'message' : 'The registrar created sucessfully'}, status=status.HTTP_201_CREATED)
            
        except serializers.ValidationError:  
            return Response({
                "message": "Validation failed",
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "message": "An unexpected error occurred",
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def get(self, request):
        registrar = Advocate.objects.filter(type_of_user='registrar')
        serializer = RegistrarSerializer(registrar, many = True)
        return Response(serializer.data,status= status.HTTP_200_OK)
    
    def delete(self, request, id):
        try:
            registrar=Advocate.objects.get(id=id,type_of_user='registrar')
            registrar.delete()
            return Response({"message" : "Registart deleted sucessfully"})
        
        except Advocate.DoesNotExist:
            return Response({"message" : "The Registrar cout not be found"})
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred",
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def patch(self, request, id):
        try:
            registrar=Advocate.objects.get(id=id,type_of_user='registrar')
            serializer = RegistrarSerializer(registrar, data=request.data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Registrar details updated sucessfully"},status=status.HTTP_200_OK)
            return Response({"message" : "Registrar could not be found"},status=status.HTTP_400_BAD_REQUEST)
        except Advocate.DoesNotExist:
            return Response({"message" : "Registrar could not be found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message" : "An unexcepted error occured "},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class RegistrarSuspendView(APIView):
    def patch(self, request, id):
        try :
            registrar = Advocate.objects.get(id = id)
            serializer=RegistrarSerializer(Advocate)
            registrar.is_suspend = not registrar.is_suspend
            registrar.save()

            if registrar.is_suspend:
                return Response({"message" : "Registrar suspended sucessfully",  "data":serializer.data}, status = status.HTTP_202_ACCEPTED)
            return Response({"message" : "Registrar suspension removed sucessfully", "data":serializer.data}, status = status.HTTP_202_ACCEPTED)

        except Advocate.DoesNotExist:
            return Response({
                "message" : "Registrar could not be found"
                }, status= status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred",
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



 