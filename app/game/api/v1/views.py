from django.shortcuts import get_object_or_404
from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from game.api.v1.serializers import GameSerializer
from listing.api.v1.serializers import GameListingsSerializer
from game.models import Game


# Create your views here.

class GameSearchView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameListingsSerializer
    permission_classes = (AllowAny,)
    lookup_field = "id"

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # Perform the lookup filtering.
        lookup_value = self.kwargs.get(self.lookup_field, None)
        if lookup_value:
            filter_kwargs = {self.lookup_field: lookup_value}
        else:
            filter_kwargs = {'slug': self.kwargs['slug']}
        obj = get_object_or_404(queryset, **filter_kwargs)
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj


class GameListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        category = self.request.GET.get('category', None)
        qs = Game.objects.all()
        if category:
            return qs.filter(category=category)
        return qs


class GameRegisterView(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        data = request.data
        print(data)
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            serializer.save()
            response_data = {
                'message': 'Your game listing was created successfully',
                'game_listing': serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        print("serializer.errors: ", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








