from django.db import models

# Create your models here

class WeatherStation(models.Model):
    name = models.CharField(max_length=100)
    station_id = models.CharField(max_length=50, unique=True)
    access_token = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WeatherData(models.Model):
    station = models.ForeignKey(WeatherStation, on_delete=models.CASCADE)
    station_name = models.CharField(max_length=64, default="fluffy", null=True)
    pressure_trend = models.CharField(max_length=30, default="none")
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.IntegerField(default=0)
    feels_like = models.FloatField(default=0)
    wind_chill = models.FloatField(default=0)
    heat_index = models.FloatField(default=0)
    sea_level_pressure = models.FloatField(default=0)
    wind_gust = models.FloatField(default=0)
    dew_point = models.FloatField(default=0)
    updated_at = models.DateTimeField()
