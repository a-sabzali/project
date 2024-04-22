from django.urls import path
from blog.views import PersonListCreateView, PersonRetrieveUpdateDestroyView

urlpatterns = [
    path('', PersonListCreateView.as_view()),
    path('<int:pk>/', PersonRetrieveUpdateDestroyView.as_view()),
]
