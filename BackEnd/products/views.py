from rest_framework.views import APIView
from .models import Product, Seller, Category

class ProductsList(APIView):
  

  pass


  def get(self, request):
    products =  Product.objects.all()
    # serializer





