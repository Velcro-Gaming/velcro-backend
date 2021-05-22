from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import update_session_auth_hash
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated

User = get_user_model()


# Create your views here.

# Change password
class PasswordChangeView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        old_password = self.request.data.get('old_password', None)
        new_password = self.request.data.get('new_password', None)
        if not old_password or old_password == "":
            raise ValidationError({'message': 'Enter your old password.'})
        if not new_password or new_password == "":
            raise ValidationError({'message': 'Enter a new password.'})
        user = request.user
        password_correct = authenticate(
            username=user.mobile, password=old_password)
        print(password_correct)
        if password_correct and new_password:
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            return Response({'message': 'Password changed successfully.'})
        raise ValidationError(
            {'message': 'Something went wrong. Check entered password.'})
