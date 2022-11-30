
from django.urls import path

from . import views

urlpatterns = [
    path('bigboy/', views.bigboy),
]