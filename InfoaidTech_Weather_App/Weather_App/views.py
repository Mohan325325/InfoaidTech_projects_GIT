from django.shortcuts import render
import requests

def get_weather_data(city):
    api_key = '2efb1393ed4151b698095c0377d8a430'
    base_url = 'http://api.openweathermap.org/data/2.5/forecast'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    k = response.json()
    return k

def weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        weather_data = get_weather_data(city)

        if 'list' in weather_data:
            forecast_data = []
            for entry in weather_data['list']:
                forecast_data.append({
                    'date': entry['dt_txt'],
                    'temperature': entry['main']['temp'],
                    'humidity': entry['main']['humidity'],
                    'wind_speed': entry['wind']['speed'],
                    'weather_condition': entry['weather'][0]['description'],
                })

            context = {'forecast_data': forecast_data}
            return render(request, 'Weather_App/weather.html', context)

    return render(request, 'Weather_App/weather.html')
