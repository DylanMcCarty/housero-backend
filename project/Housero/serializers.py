# from django.contrib.auth.models import User, Group
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser, Criteria

class UserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)

        return user

        email = serializers.EmailField(
        required=True
        )
        username = serializers.CharField()
        password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}
        depth=1
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        return token

class CriteriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Criteria
        fields = '__all__'