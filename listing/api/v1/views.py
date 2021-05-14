from django.shortcuts import render
from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import ListingSerializer, ListingsGameSerializer
from game.api.v1.serializers import GameLiteSerializer

from listing.models import Listing


# Create your views here.

class ListedGamesView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = GameLiteSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        query = kwargs.get('q', None)
        listings_qs = self.get_queryset()
        if query:
            listings_qs = listings_qs.filter(game__name__icontains=query)

        games_qs = listings_qs.values_list("game", flat=True).distinct()
        game_list = list(games_qs)
        serializer = ListingsGameSerializer(data={'games': game_list}, context={'request': request})
        if serializer.is_valid():
            # serializer.data
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (AllowAny,)
    lookup_field = "id"


class ListingListView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            qs = Listing.objects.all()
        else:
            qs = Listing.objects.filter(owner=user)
        rent = self.request.GET.get('rent', None)
        swap = self.request.GET.get('swap', None)
        sell = self.request.GET.get('sell', None)
        if rent:
            qs = qs.filter(rent=rent)
        if swap:
            qs = qs.filter(swap=swap)
        if sell:
            qs = qs.filter(sell=sell)
        return qs


class ListingCreateView(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        data = request.data
        print(data)
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            game_listing = serializer.save(owner=request.user)
            response_data = {
                'message': 'Your game listing was created successfully',
                'game_listing': serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        print("serializer.errors: ", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





