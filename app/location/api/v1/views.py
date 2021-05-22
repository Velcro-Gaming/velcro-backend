from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import CountrySerializer, StateSerializer, CitySerializer

from location.models import Country, State, City


# Create your views here.
class CountryView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)


class StateView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        country_id = self.request.GET.get('country_id', None)
        qs = State.objects.all()
        if country_id:
            return qs.filter(country__id=country_id)
        return qs


class CityView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        country_id = self.request.GET.get('country_id', None)
        state_id = self.request.GET.get('state_id', None)
        qs = City.objects.all()
        if state_id:
            return qs.filter(state__id=state_id)
        elif country_id:
            return qs.filter(state__country__id=country_id)
        return qs



