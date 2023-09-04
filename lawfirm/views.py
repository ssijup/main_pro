from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django.shortcuts import render
from rest_framework import status

from .serializer import LawFirmListSerializer
from .models import LawFirm




class LawFirmListView(APIView):
    def get(self, request):
        lawfirm = LawFirm.objects.all()
        serializer = LawFirmListSerializer(lawfirm, many = True)
        return Response(serializer.data,status= status.HTTP_200_OK)
    

    def post(self, request):
        data = request.data
        serializer = LawFirmListSerializer(data=data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message": "Lawfirm details created successfully"}, status=status.HTTP_201_CREATED)

        except serializers.ValidationError:  
            return Response({
                "message": "Validation failed",
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "message": "An unexpected error occurred",
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class SuspendLawFirmView(APIView):
    def patch(self, request, id):
        try :
            lawfirm = LawFirm.objects.get(id = id)
            serializer=LawFirmListSerializer(lawfirm)
            lawfirm.is_suspend = not lawfirm.is_suspend
            lawfirm.save()

            if lawfirm.is_suspend:
                return Response({"message" : "LawFirm suspended sucessfully",  "data":serializer.data}, status = status.HTTP_202_ACCEPTED)
            return Response({"message" : "LawFirm suspension removed sucessfully", "data":serializer.data}, status = status.HTTP_202_ACCEPTED)

        except LawFirm.DoesNotExist:
            return Response({
                "message" : "LawFirm could not be found"
                }, status= status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred",
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class DeletelawFirmView(APIView):
    def delete(self, request, id):
        try:
            lawfirm=LawFirm.objects.get(id=id)
            lawfirm.delete()
            return Response({"message" : "LawFirm deleted sucessfully"})
        
        except LawFirm.DoesNotExist:
            return Response({"message" : "The LawFirm cout not be found"})
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred",
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EditLawfirmView(APIView):
    def patch(self, request, id):
        try:
            lawfirm=LawFirm.objects.get(id=id)
            serializer = LawFirmListSerializer(lawfirm, data=request.data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Lawfirm details updated sucessfully"},status=status.HTTP_200_OK)
            return Response({"message" : "Lawfirm could not be found"},status=status.HTTP_400_BAD_REQUEST)
        except LawFirm.DoesNotExist:
            return Response({"message" : "Lawfirm could not be found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message" : "An unexcepted error occured "},status=status.HTTP_500_INTERNAL_SERVER_ERROR)