"""
В этом файле будут создаваться классы,
которые преобразуют данные моделей в JSON и обратно.
Этот сериализатор будет использоваться для обработки данных модели Flight.
"""

from rest_framework import serializers
from .models import Flight, Airport


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'
