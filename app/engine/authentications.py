from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserAuthentication(object):
    def authenticate(self, request, username_email=None, password=None):
        try:
            user = User.objects.get(username=username_email)
        except:
            try:
                user = User.objects.get(email=username_email)
            except:
                user = None

        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except:
            return None
