from django.contrib.auth import authenticate, get_user_model

from rest_framework import generics, views, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from accounts.mixins import JsonWebTokenMixin
from accounts.api.v1.serializers import (
    UserSerializer,
    UserRUDSerializer, 
    UserLoginSerializer
)


# Create your views here.

User = get_user_model()


# User Login
class LoginView(JsonWebTokenMixin, views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            username_email = validated_data.get("username_email")
            password = validated_data.get("password")
            user = authenticate(username_email=username_email, password=password)
            if user:
                token = self.get_jwt_token(user)
                data = {
                    'message': 'User logged in successfully',
                    'token': token,
                    'user': UserSerializer(user).data,
                }
                return Response(data, status=status.HTTP_200_OK)
            error_data = {'message': 'incorrect credentials'}
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Create View
class UserCreateView(JsonWebTokenMixin, views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        print(data)
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = self.get_jwt_token(user)
            response_data = {
                'message': 'Account created successfully',
                'token': token,
                'user': UserSerializer(user).data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
