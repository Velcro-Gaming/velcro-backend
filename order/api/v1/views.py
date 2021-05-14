from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import OrderSerializer

from order.models import Order


# Create your views here.

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (AllowAny,)
    lookup_field = "id"


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        order_type = self.request.GET.get('order_type', None)
        qs = Order.objects.all()
        if order_type:
            return qs.filter(_type=order_type)
        return qs


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (AllowAny,)




