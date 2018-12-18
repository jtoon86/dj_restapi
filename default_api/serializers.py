from rest_framework import serializers
from . import models


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'number', 'description', 'created_by_user', 'modified_by_user', 'is_system', 'is_active')
        model = models.Order
