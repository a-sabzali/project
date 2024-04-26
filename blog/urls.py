from django.urls import path
from blog.views import PersonListCreateView, PersonRetrieveUpdateDestroyView,\
    ProductListCreateView, ProductRetrieveUpdateDestroyView, CategoryListCreateView,\
    CategoryRetrieveUpdateDestroyView

urlpatterns = [

    path('', ProductListCreateView.as_view()),
    path('<int:pk>/', ProductRetrieveUpdateDestroyView.as_view()),

    path('person/', PersonListCreateView.as_view()),
    path('person/<int:pk>/', PersonRetrieveUpdateDestroyView.as_view()),

    path('category/', CategoryListCreateView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view()),
]
