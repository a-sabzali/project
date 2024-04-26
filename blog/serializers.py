from blog.models import Person, Product, Category
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'available',
                  'created_at', 'numbers', 'discount')
