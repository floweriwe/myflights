from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Airport(models.Model):  # Содержит информацию об аэропортах, необходимую для поиска рейсов.
    iata_code = models.CharField(max_length=3, unique=True)  # Например, NQZ
    name = models.CharField(max_length=100)  # Например, 'Международный аэропорт имени Нурсултана Назарбаева'
    city = models.CharField(max_length=100)  # Например, 'Астана'
    country = models.CharField(max_length=100)  # Например, 'Казахстан'

    def __str__(self):
        return f"{self.name} ({self.iata_code})"


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)  # например, 'USD', 'EUR'
    name = models.CharField(max_length=30)  # например, 'US Dollar', 'Euro'


class Flight(models.Model):  # Представляет информацию о конкретном рейсе
    flight_number = models.CharField(max_length=10)  # Например, 'SU123'
    airline = models.CharField(max_length=100)  # Например, 'Аэрофлот'
    departure_airport = models.ForeignKey(Airport, related_name='departures', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    seats_available = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.airline} {self.flight_number}"


class Booking(models.Model):  # Хранит информацию о бронировании рейса пользователем.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passengers = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, choices=[
        ('Pending', 'В ожидании'),
        ('Confirmed', 'Подтверждено'),
        ('Canceled', 'Отменено'),
    ], default='Pending')

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"


class SearchQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    departure_airport = models.ForeignKey(Airport, related_name='search_departures', on_delete=models.CASCADE)
    departure_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    passengers = models.PositiveIntegerField(default=1)
    max_stay_duration = models.PositiveIntegerField(help_text="Максимальное количество дней пребывания")
    search_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Search by {self.user.username if self.user else 'Anonymous'} on {self.search_date}"

