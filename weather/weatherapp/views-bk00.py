from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f4a2e2c54390e772661177ace2831a36'

    cities = City.objects.all() #return all the cities in the database

    if request.method == 'POST': #only true if form is submitted
        form = CityForm(request.POST) #add actural request data to form for processing
        form.save() #will validate and save if validate

    form = CityForm()

    weather_data = []
    
    for city in cities:
        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        #print(city_weather)

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'weatherapp/index.html', context) #returns the index.html template
