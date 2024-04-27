from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import Person, Product, Category
from blog.serializers import PersonSerializer, ProductSerializer, CategorySerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
       This ViewSet automatically provides `list`, `create`, `retrieve`,
       `update` and `destroy` actions.
    """

    permission_classes = (IsAuthenticatedOrReadOnly, )

    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
       This ViewSet automatically provides `list`, `create`, `retrieve`,
       `update` and `destroy` actions.
    """

    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
       This ViewSet automatically provides `list`, `create`, `retrieve`,
       `update` and `destroy` actions.
    """

    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
