from django.shortcuts import render
from .models import CustomUser1
from .serializers import CustomUser1Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class CustomUser1ListView(APIView):
    def get(self,request,id=None):
        if id is not None:
            queryset = CustomUser1.objects.get(id = id)
            if queryset:
                serializer = CustomUser1Serializer(queryset)
                return Response({'status':status.HTTP_200_OK,'data':serializer.data,'message':'success'})
            return Response({'status':status.HTTP_400_BAD_REQUEST})
        else:
            queryset = CustomUser1.objects.all()
            if queryset:
                serializer = CustomUser1Serializer(queryset,many=True)
                return Response({'status': status.HTTP_200_OK, 'data': serializer.data, 'message': 'success'})
            return Response({'status': status.HTTP_400_BAD_REQUEST})

    def post(self,request):
        serializer = CustomUser1Serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':status.HTTP_201_CREATED,'data':serializer.data,'message':'success'})
        return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'failure','error':serializer.errors})
