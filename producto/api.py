from rest_framework.response import Response
from rest_framework.views import APIView

from producto.models import Producto
from producto.serializers import ProductoSerializer, ProductoListSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class ProductoListAPI(ListCreateAPIView):
    queryset = Producto.objects.all()

    def get_serializer_class(self):
        return ProductoSerializer if self.request.method == "POST" else ProductoListSerializer


class ProductoDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
