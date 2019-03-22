import requests

from django.shortcuts import render
from django.views import View

from .models import City
from .forms import CityForm

API_KEY = '0a136f3cef869764f8d63741dbac7973'

class HomeView(View):
    def get(self, request, *args, **kwargs):
        """
            Get your own API Key by signing up on OpenMapWeather
            URL - https://home.openweathermap.org/users/sign_up
        """
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + API_KEY

        form = CityForm()

        cities = City.objects.all()
        weather_data = []

        for city in cities:
            r = requests.get(url.format(city)).json()

            city_weather = {
                'city': city.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
            weather_data.append(city_weather)

        context = {
            'weather_data': weather_data,
            'form': form
        }

        return render(request, 'weather/weather.html', context)

    def post(self, request, *args, **kwargs):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + API_KEY

        form = CityForm(request.POST)
        form.save()

        form = CityForm()

        cities = City.objects.all()
        weather_data = []

        for city in cities:
            r = requests.get(url.format(city)).json()

            city_weather = {
                'city': city.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
            weather_data.append(city_weather)

        context = {
            'weather_data': weather_data,
            'form': form,
        }

        return render(request, 'weather/weather.html', context)
