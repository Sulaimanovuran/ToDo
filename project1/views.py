from django.shortcuts import render

# Create your views here.
from rest_framework.generics import *

from project1.models import BuyProduct
from project1.serializers import BuyProductSerializers


class BuyProductListView(ListAPIView):
    queryset = BuyProduct.objects.all()
    serializer_class = BuyProductSerializers


class BuyProductCreateView(CreateAPIView):
    serializer_class = BuyProductSerializers


class BuyProductDetailView(RetrieveAPIView):
    queryset = BuyProduct.objects.all()
    serializer_class = BuyProductSerializers


class BuyProductUpdateView(UpdateAPIView):
    queryset = BuyProduct.objects.all()
    serializer_class = BuyProductSerializers


class BuyProductDeleteView(DestroyAPIView):
    queryset = BuyProduct.objects.all()
