
from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from django.contrib import admin
from .views import ObtainTokenPairWithColorView, CustomUserCreate, CriteriaAPIView

urlpatterns = [
    path('user/', CustomUserCreate.as_view(), name="create_user"),
    path('user/<str:pk>/', CustomUserCreate.as_view()),
    # path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),  
    path('criteria/<str:pk>/', CriteriaAPIView.as_view()),
    path('criteria/', CriteriaAPIView.as_view()),
]


