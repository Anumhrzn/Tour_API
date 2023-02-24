import requests

api_key = 'bea6e27c01ba8b40b29fc55a918cb0e0'


def get_locations(location):
    weather_data = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={location} &units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        print("No City Found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])

        print(f"The weather in {location} is: {weather}")
        print(f"The temperature in {location} is: {temp}ºF")
        return weather, temp
