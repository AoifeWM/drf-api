from django.shortcuts import render
from rest_framework import generics
from .serializer import SaleSerializer
from .models import Sale


class SaleList(generics.ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleDetail(generics.RetrieveAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer