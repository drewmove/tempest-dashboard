from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import WeatherStation

@admin.register(WeatherStation)
class WeatherStationAdmin(admin.ModelAdmin):
    list_display = ('name', 'station_id', 'access_token')
