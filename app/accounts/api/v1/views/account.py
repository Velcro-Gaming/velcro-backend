from django.contrib.auth import authenticate, get_user_model

from rest_framework import generics, views, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from accounts.mixins import JsonWebTokenMixin
from accounts.api.v1.serializers import (
    UserSerializer,
    UserRUDSerializer, 
    UserLoginSerializer,
    ExtraRegistrationSerializer
)
from console.models import Console, UserConsole
from engine.permissions import IsAgentOrStaff

# Create your views here.

User = get_user_model()
           

# User Retrieve, Update and Delete
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRUDSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'


# User Extra Registration
class UserExtraRegistrationView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        user = request.user
        error_messages = []
        serializer = ExtraRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            print("validated_data: ", validated_data)

            console_id = validated_data.get("console", None)
            if console_id:
                try:
                    console = Console.objects.get(id=console_id)
                except:
                    error_messages.append("Invalid console")
                    return Response({"console": error_messages}, status=status.HTTP_400_BAD_REQUEST)
                #
                print("console: ", console)

                user_console, _ = UserConsole.objects.get_or_create(
                    user=user, console=console
                )

            nin = validated_data.get("nin", None)
            # DO SOMETHING
            print("nin: ", nin)

            referal_code = validated_data.get("referal_code", None)
            # DO SOMETHING
            print("referal_code: ", referal_code)


            data = {
                "message": "User updated successfully",
                "user": UserSerializer(user).data
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User List View
class UserListView(generics.ListAPIView):
    queryset = User.objects.all().exclude(is_admin=True, is_staff=True)
    serializer_class = UserSerializer
    permission_classes = (IsAgentOrStaff,)



