from django.contrib.auth import get_user_model
from django.contrib.auth import hashers
from rest_framework import serializers

from console.api.v1.serializers import UserConsoleSerializer
from engine.utils import parse_full_name, process_mobile_number, process_email_address, unique_mobile_number_generator

User = get_user_model()


class UserLiteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
                'id', 'username',
                'first_name', 'last_name', 'full_name',
                'email', 'mobile'
            )

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    consoles = serializers.SerializerMethodField()
    verification = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = (
                'id', 'username',
                'first_name', 'last_name', 'full_name',
                'email', 'mobile', 'mobile_verified', 
                'verification',
                'consoles',
                'referral_code',
                'is_admin', 'is_staff',
                'created_at', 'updated_at',
                'password',
            )
        extra_kwargs = {
            'email': {'required': False},
        }

    def get_consoles(self, user):
        user_console_list = user.consoles.all()
        return UserConsoleSerializer(user_console_list, many=True).data

    def get_verification(self, user):
        return user.verification.get_status_display()

    def validate_mobile(self, value):
        valid, mobile = process_mobile_number(value)
        if valid:
            # Check if number exists
            qs = User.objects.filter(mobile=mobile)
            if qs.exists():
                user = qs.first()
                if user.is_bar_man:
                    pass
                else:
                    raise serializers.ValidationError(
                        "User with this phone number exists already.")
            return mobile
        raise serializers.ValidationError(
            "Confirm number is valid and try again.")

    def validate_email(self, value):
        if value:
            valid, email = process_email_address(value)
            if not valid:
                raise serializers.ValidationError("Enter a vaid email address")
            # Check if exists
            user_email_qs = User.objects.filter(email=email)
            if user_email_qs.exists():
                raise serializers.ValidationError(
                    "User with this email exists")
            return email
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ExtraRegistrationSerializer(serializers.Serializer):
    console = serializers.CharField(write_only=True)
    referal_code = serializers.CharField(write_only=True, required=False)
    nin = serializers.CharField(write_only=True, required=False)


class UserLoginSerializer(serializers.Serializer):
    username_email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    
    def validate_username_email(self, username_email):
        valid, email = process_email_address(username_email)
        if valid:
            user_qs = User.objects.filter(email=email)
            if not user_qs.exists():
                raise serializers.ValidationError(
                    "User with this email does not exists")
            return email

        user_qs = User.objects.filter(username=username_email)
        if not user_qs.exists():
            raise serializers.ValidationError(
                "User with this username does not exists")
        return username_email


class UserRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name', 'last_name',
            'email', 'mobile',
        ]

        