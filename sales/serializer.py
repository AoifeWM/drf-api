from rest_framework import serializers
from .models import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'quantity', 'price_each', 'time', 'purchaser')
        model = Sale
