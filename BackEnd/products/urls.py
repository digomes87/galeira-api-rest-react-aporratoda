from django.urls import path
from .views import ProductList

urlpatterns = [
  path('products', ProductsList.as_view()),
]
