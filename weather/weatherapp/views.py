from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f4a2e2c54390e772661177ace2831a36'

    cities = City.objects.all() #return all the cities in the database

    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            try:
                response = requests.get(url.format(city_name))
                #response.raise_for_status()
                city_weather = response.json()

                if city_weather.get('cod') == 200:  # Only save valid cities
                    form.save()
                else:
                    messages.error(request, "Invalid city name. Please enter a valid city.")
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")

            # Redirect to avoid form resubmission on page refresh
            return redirect('index')

    form = CityForm()
    weather_data = []

    for city in cities:
        try:
            city_weather = requests.get(url.format(city)).json()

            if city_weather.get('cod') == 200:
                # Safely access keys with default values
                weather = {
                    'city': city,
                    'temperature': city_weather.get('main', {}).get('temp', 'N/A'),
                    'description': city_weather.get('weather', [{}])[0].get('description', 'N/A'),
                    'icon': city_weather.get('weather', [{}])[0].get('icon', '')
                }
                weather_data.append(weather)
            else:
                messages.error(request, f"Weather data not found for {city}.")
        except Exception as e:
            messages.error(request, f"Error fetching weather for {city}: {e}")

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weatherapp/index.html', context)

    