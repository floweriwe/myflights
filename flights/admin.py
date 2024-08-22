from django.contrib import admin
from .models import Flight, Airport, Currency, Booking, SearchQuery

admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Currency)
admin.site.register(Booking)
admin.site.register(SearchQuery)