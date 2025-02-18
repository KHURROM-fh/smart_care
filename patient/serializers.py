from rest_framework import serializers
from .models import Patinet  
from django.contrib.auth.models import User


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patinet
        fields = '__all__'

class RegistationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password')  # Remove confirm_password before creating user
        password = validated_data['password']

        if password != confirm_password:
            raise serializers.ValidationError({"error": "Passwords do not match"})

        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({"error": "Email already exists"})

        user = User.objects.create_user(**validated_data)  # Use create_user to handle password hashing
        user.is_active= False
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username= serializers.CharField(required= True)
    password= serializers.CharField(required= True)