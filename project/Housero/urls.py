
from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views
from django.contrib import admin
from .views import ObtainTokenPairWithColorView, CustomUserCreate, CriteriaAPIView, LikedHousesModelView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'criteria', views.CriteriaAPIView)
router.register(r'liked', views.LikedHousesModelView)
# router.register(r'fixliked/<int:fk>/<int>', views.FixLikedHousesModelView)

urlpatterns = [
    path('', include(router.urls)),
    path('user/', CustomUserCreate.as_view(), name="create_user"),
    path('user/<str:pk>/', CustomUserCreate.as_view()),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'), 
]


