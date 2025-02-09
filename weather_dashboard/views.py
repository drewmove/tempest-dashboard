import requests
from django.shortcuts import render
from .models import WeatherStation, WeatherData
from datetime import datetime
from datetime import timezone
from zoneinfo import ZoneInfo
import time



 
def dashboard(request):
    stations = WeatherStation.objects.all()
    for station in stations:
        urlstring = f"https://swd.weatherflow.com/swd/rest/observations/station/{station.station_id}?token={station.access_token}"
        print(f"URL String {urlstring}")
        response = requests.get(urlstring
        )
        if response.status_code == 200:
            print(f"API Response 200 OK from Tempest {urlstring}")
            data = response.json()
            #print(f"Json {data}")
            obs = data['obs'][0]
            rawtemp = obs.get('air_temperature')
            localtemp = round(rawtemp * 5 / 9 + 32,2)
            rawwind_chill = obs.get('wind_chill')
            rawfeels_like = obs.get('feels_like')
            rawheat_index = obs.get('heat_index')
            rawdew_point = obs.get('dew_point')
            rawwind_gust = obs.get('wind_gust')
            localheat_index = round(rawheat_index*5/9+32,2)
            localwind_chill = round(rawwind_chill*5/9+32,2)
            localfeels_like = round(rawfeels_like*5/9+32,2)
            localdew_point = round(rawdew_point*5/9+32,2)

            rawwind = obs.get('wind_avg')
            localwind = round(rawwind * 1.94384,2)
            localwind_gust = round(rawwind_gust * 1.94384,2)
            localtzname = data.get('timezone')
            localtime= obs.get('timestamp')
            rawpressure = obs.get('sea_level_pressure')
                       
            #localtime = localtime - 1440
            
            #localtime = datetime.utcfromtimestamp(obs.get('timestamp'))

            localdt = datetime.fromtimestamp(localtime, tz=ZoneInfo(localtzname))
            
            print(f"Local: {localdt} TZ: {localtzname}")
           
            

            print(f"Station: {station.station_id}")
            WeatherData.objects.update_or_create(
                station=station,
                defaults={
                    'station_name': data.get('station_name'),
                    'pressure_trend': obs.get('pressure_trend'),
                    #'temperature': obs.get('air_temperature'),
                    'temperature': localtemp,
                    'dew_point': localdew_point,
                    'humidity': obs.get('relative_humidity'),
                    'wind_speed': localwind,
                    'wind_chill': localwind_chill,
                    'feels_like': localfeels_like,
                    'heat_index': localheat_index,
                    'wind_direction': obs.get('wind_direction'),
                    'sea_level_pressure': rawpressure,
                    'wind_gust': localwind_gust,
                    'updated_at': localdt,
                },
            )

    weather_data = WeatherData.objects.filter(station__in=stations)
    return render(request, 'weather_dashboard/dashboard.html', {'stations': stations, 'weather_data': weather_data})

#from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render
#from .models import WeatherStation, WeatherData

#def dashboard(request):
#    stations = WeatherStation.objects.all()
#    data = WeatherData.objects.filter(station__in=stations)
#    return render(request, 'weather_dashboard/dashboard.html', {'stations': stations, 'data': data})

