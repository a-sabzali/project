from django.urls import path, include
from blog.views import PersonViewSet, CategoryViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'person', PersonViewSet, basename='person')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls))
]
