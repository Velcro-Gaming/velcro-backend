from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import ConsoleSerializer, UserConsoleSerializer

from console.models import Console, UserConsole


# Create your views here.

class UserConsoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserConsole.objects.all()
    serializer_class = UserConsoleSerializer
    permission_classes = (AllowAny,)
    lookup_field = "id"


class UserConsoleListView(generics.ListAPIView):
    queryset = UserConsole.objects.all()
    serializer_class = UserConsoleSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        user = self.kwargs.get('user', None)
        return UserConsole.objects.filter(user=user)


class UserConsoleRegisterView(generics.CreateAPIView):
    queryset = UserConsole.objects.all()
    serializer_class = UserConsoleSerializer
    permission_classes = (AllowAny,)





class ConsoleDetailView(generics.RetrieveAPIView):
    queryset = Console.objects.all()
    serializer_class = ConsoleSerializer
    permission_classes = (AllowAny,)
    lookup_field = "id"


class ConsoleListView(generics.ListAPIView):
    queryset = Console.objects.all()
    serializer_class = ConsoleSerializer
    permission_classes = (AllowAny,)
