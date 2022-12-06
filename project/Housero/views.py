from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import CustomUser, Criteria
from rest_framework import viewsets
from rest_framework import permissions
from Housero.serializers import UserSerializer, MyTokenObtainPairSerializer, CriteriaSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from .models import Criteria

# Create your views here.



class ObtainTokenPairWithColorView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = UserSerializer(data)
        else:
            data = CustomUser.objects.all()
            serializer = UserSerializer(data, many=True)
        return Response(serializer.data)



class CriteriaAPIView(APIView):

    def get_object(self, pk):
        try:
            return Criteria.objects.get(pk=pk)
        except Criteria.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = CriteriaSerializer(data)
        
        else:
            data = Criteria.objects.all()
            serializer = CriteriaSerializer(data, many=True)
        return Response(serializer.data)

    def put(self, request, pk=None, format=None):
        criteria_to_update = Criteria.objects.get(pk=pk)
        data = request.data
        serializer = CriteriaSerializer(instance=criteria_to_update, data=data, partial=True) 

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response.data = {
            'message': 'Criteria Updated Succesfully',
            'data': serializer.data
        }

        return response

