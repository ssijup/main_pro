from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import status
from .serializer import AdvocatesListSerializer
from rest_framework import serializers
from userapp.models import Advocate

class AdvocatesListView(APIView):
    def get(self, request):
        advocates = Advocate.objects.all()
        serializer = AdvocatesListSerializer(advocates, many = True)
        return Response(serializer.data,status= status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = AdvocatesListSerializer(data=data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message": "Advocate details created successfully"}, status=status.HTTP_201_CREATED)
        except serializers.ValidationError:  
            return Response({
                "message": "Validation failed",
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred. Please try again later"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class SuspendAdvocateView(APIView):
    def patch(self, request, id):
        try :
            advocate = Advocate.objects.get(id = id)
            serializer=AdvocatesListSerializer(advocate)
            advocate.is_suspend = not advocate.is_suspend
            advocate.save()

            if advocate.is_suspend:
                return Response({"message" : "Advocate suspended successfully" ,"data":serializer.data}, status = status.HTTP_202_ACCEPTED)
            return Response({"message" : "Advocate suspension removed successfully" ,"data":serializer.data}, status = status.HTTP_202_ACCEPTED)

        except Advocate.DoesNotExist:
            return Response({
                "message" : "Advocate does not found"
                }, status= status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred "
                
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
    

class EditAdvocateProfileView(APIView):
    def patch(self, request, id): 
        try:
            advocate=Advocate.objects.get(id=id)
            serializer = AdvocatesListSerializer(advocate, data=request.data, Partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Advocate details updated sucessfully"},status=status.HTTP_200_OK)
            return Response({"message" : "Validation failed"},status=status.HTTP_400_BAD_REQUEST)
        except Advocate.DoesNotExist:
            return Response({"message" : "Advocate could not be found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message" : "An unexcepted error occured "},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AdvocateEditFormView(APIView):
    def get(self, request, id) :
        try:
            advocate=Advocate.objects.get(id=id)
            serializer=AdvocatesListSerializer(advocate)
            return Response(serializer.data ,status=status.HTTP_200_OK)

        except Advocate.DoesNotExist:
                    return Response({
                         "message" : "Advocate  could not be found"
                         },status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
                    return Response({
                        "message": "An unexpected error occurred "  
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)