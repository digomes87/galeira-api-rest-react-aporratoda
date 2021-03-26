from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Product, Seller, Category
from .serializers import ProductSerializer, ProductsAllInfoSerializer, CategorySerializer, SellerSerializer

class ProductsList(APIView):



  def get(self, request):
    products =  Product.objects.all()
    serializer = ProductsAllInfoSerializer(products, many=True)
    return Response(serializer.data)



  def post(self, request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryViewSet(ModelViewSet):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()

class SellerViewSet(ModelViewSet):
  serializer_class = SellerSerializer
  queryset = Seller.objects.all()

