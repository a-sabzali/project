from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView

from blog.models import Person, Product, Category
from blog.serializers import PersonSerializer, ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PersonListCreateView(ListCreateAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CategoryListCreateView(ListCreateAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListCreateView(ListCreateAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
