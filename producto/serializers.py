# -*- coding: utf-8 -*-
from rest_framework import serializers
from producto.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        exclude = []


class ProductoListSerializer(ProductoSerializer):
    class Meta(ProductoSerializer.Meta):
        fields = ( 'id','imagen', 'nombre', 'precio', 'descripcion',)
