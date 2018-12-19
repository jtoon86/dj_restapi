from rest_framework import generics

from . import models
from .serializers import OrderSerializer, LineSerializer, OrderSerializerBasic


# Create your views here.
class OrderList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    # serializer_class = OrderSerializer
    filter_fields = ('number', 'description')

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return OrderSerializer
        return OrderSerializerBasic


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()

    # serializer_class = OrderSerializer

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return OrderSerializer
        return OrderSerializerBasic


class ItemList(generics.ListCreateAPIView):
    queryset = models.Line.objects.all()
    serializer_class = LineSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Line.objects.all()
    serializer_class = LineSerializer
