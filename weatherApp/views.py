import datetime
import datetime
import requests
from django.shortcuts import render

# Create your views here.

def home(request):
    weather = {}
    error = None

    if request.method == 'POST':
        city = request.POST.get('city', 'London')  # Default to London if city is empty
        api_key = 'e0fe587fdb8f6f7c0b6e19a6fbae0fff'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': city,
                'temperature': data['main']['temp'],
                'condition': data['weather'][0]['description'].title(),
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            error = "City not found."

    day = datetime.date.today()
    return render(request, 'index.html', {
        'weather': weather,
        'error': error,
        'day': day
    })
