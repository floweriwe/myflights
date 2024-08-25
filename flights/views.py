from rest_framework import viewsets
from .models import Flight, Airport
from .serializers import FlightSerializer, AirportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import logging


# Этот класс FlightViewSet будет управлять CRUD-операциями для модели Flight.
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightSearchView(APIView):
    def get(self, request):
        # Пример фильтрации по аэропортам и дате
        from_airport = request.query_params.get('from')
        to_airport = request.query_params.get('to')
        departure_date = request.query_params.get('departure_date')
        return_date = request.query_params.get('return_date')

        # Логика поиска билетов через API или БД
        flights = []  # Здесь будет список найденных билетов
        logging.debug("Exiting FlightSearchView.get")

        return Response(flights)


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
