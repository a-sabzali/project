from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView

from blog.models import Person
from blog.serializers import PersonSerializer


class PersonListCreateView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
