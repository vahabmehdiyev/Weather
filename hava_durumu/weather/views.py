import requests
from django.shortcuts import render
from .models import City

def get_weather(request):
    api_key = '89084306a2ac918f5faa263187b957ca'  # OpenWeatherMap API anahtarını buraya yapıştırın

    city = 'Istanbul'  # Hava durumu verilerini çekmek istediğiniz şehri burada belirleyin

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_status = data['weather'][0]['description']

    city = City.objects.create(name=city, temperature=temperature, humidity=humidity, weather_status=weather_status)

    context = {'city': city}
    return render(request, 'weather.html', context)
