from rest_framework import viewsets
from .models import Flight
from .serializers import FlightSerializer


# Этот класс FlightViewSet будет управлять CRUD-операциями для модели Flight.
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
