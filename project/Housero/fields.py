from .models import *
from rest_framework import serializers

class CustomUserListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.id

    def to_internal_value(self, data):
        return CustomUser.objects.get(id=data)

