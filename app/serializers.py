
from rest_framework import serializers
from . import models
from django.contrib.auth import authenticate

# User authentication ---------------------------------------------------------------------- 

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True) 
    class Meta:
        model = models.CustomUser
        fields = ['username', 'email', 'password', 'confirm_password', 'first_name', 'last_name']  # Adding confirm_password back to the fields list

    
    def validate(self, attrs):
        if attrs['password'] != self.initial_data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = models.CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
    
# ---------------------------------------------------------------------------------

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MdlTask
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at']