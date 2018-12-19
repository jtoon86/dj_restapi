from rest_framework import serializers

from . import models


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'sku', 'description', 'quantity', 'price', 'uom', 'sub_total', 'is_taxable')
        read_only_fields = ('sub_total',)
        model = models.Line


class LineSerializerBasic(serializers.ModelSerializer):
    class Meta:
        fields = ('sku', 'description', 'quantity', 'price', 'uom', 'sub_total')
        read_only_fields = ('sub_total',)
        model = models.Line


class OrderSerializer(serializers.ModelSerializer):
    lines = LineSerializer(many=True)

    class Meta:
        fields = ('id', 'number', 'description', 'created_by_user', 'modified_by_user', 'is_system',
                  'is_active', 'lines')
        model = models.Order
        depth = 1

    def create(self, validated_data):
        lines = validated_data.pop('lines')
        order = models.Order.objects.create(**validated_data)
        for line in lines:
            models.Line.objects.create(order=order, **line)
        return order


class OrderSerializerBasic(serializers.ModelSerializer):
    lines = LineSerializerBasic(many=True)

    class Meta:
        fields = ('number', 'description', 'lines')
        model = models.Order
        depth = 1

    def create(self, validated_data):
        lines = validated_data.pop('lines')
        order = models.Order.objects.create(**validated_data)
        for line in lines:
            models.Line.objects.create(order=order, **line)
        return order
