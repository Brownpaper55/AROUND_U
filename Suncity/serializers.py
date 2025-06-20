from rest_framework import serializers
from .models import Program, CustomUser
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    "serializer for customuser model"
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'is_active']
        read_only_fields = ['id','date_joined']


class CustomUserCreateSerializer(serializers.ModelSerializer):
    "serializers for creating custom users"
    password = serializers.CharField(write_only = True, min_length = 8)
    password_confirm = serializers.CharField(write_only = True, min_length = 8)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password_confirm']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError('Passwords dont match')
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = CustomUser.objects.create_user(**validated_data)
        return user


class ProgramSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only = True)
    class Meta:
        model = Program
        fields = ['name','Location','Date','Dress_code','Venue','Description','start_time','cover_photo','user']

    def validate_Date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Program date cannot be in the past")
        return value
    
    def create_program(self, validated_data):
        if 'user_id' not in validated_data:
            validated_data['user'] = self.context['request'].user
        return super().create(**validated_data)
        

class ProgramListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for listing programs"""
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Program
        fields = [
            'id', 'name', 'Location', 'Date', 'start_time', 
            'cover_photo', 'user_username', 'views'
        ]


class ProgramDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for individual program views"""
    user = CustomUserSerializer(read_only=True)
    
    class Meta:
        model = Program
        fields = [
            'id', 'name', 'Location', 'Date', 'Dress_code', 
            'Description', 'start_time', 'cover_photo', 
            'user', 'views'
        ]


