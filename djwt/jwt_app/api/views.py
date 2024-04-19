from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from jwt_app.api.serializers import CategorySerializer, ProductSerializer
from jwt_app.models import Category, Product


class CategoryAPIList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

class ProductAPIList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)