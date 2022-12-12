from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import CustomUser, Criteria, LikedHouses
from rest_framework import viewsets, permissions, status
from Housero.serializers import UserSerializer, MyTokenObtainPairSerializer, CriteriaSerializer, LikedHousesSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .models import Criteria
from django_filters.rest_framework import DjangoFilterBackend

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



class CriteriaAPIView(viewsets.ModelViewSet):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']

    # def get_object(self, pk):
    #     try:
    #         liked_house = LikedHouses.objects.get(id=request.id)
    #         liked_house.user_id = 1
    #     except LikedHouses.DoesNotExist:
    #         raise Http404
        

# class FixLikedHousesModelView(APIView):
#     queryset = LikedHouses.objects.all()
#     serializer_class = LikedHousesSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['user_id']

#     def post(self, request, format=None):
#         data = request.data
#         serializer = UsersSerializer(data=data)

#         serializer.is_valid(raise_exception=True)

#         serializer.save()

#         response = Response()

#         response.data = {
#             'message' : 'User created succesfully',
#             'data' : serializer.data,
#         }

#         return response

class LikedHousesModelView(viewsets.ModelViewSet):
    queryset = LikedHouses.objects.all()
    serializer_class = LikedHousesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id', 'house_id']



    # def post(self, request, format='json'):
    #     serializer = LikeHousesSerializer(data=request.data)
    #     if serializer.is_valid():
    #         liked = serializer.save()
    #         if user:
    #             json = serializer.data
    #             return Response(json, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

