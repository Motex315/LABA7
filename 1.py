import requests
import json

API = '8a7d0771a3e8e8fadc1955e37878cca8'
city_name = 'Cherepovets'

def get_coords(city):
    coord_url=(f'http://api.openweathermap.org/geo/1.0/direct?'
               +f'q={city}&limit=5&appid={API}')
    response = requests.get(coord_url)
    inf = json.loads(response.text)[0]
    return inf['lat'], inf['lon'], inf['local_names']['ru'] 

def get_weather(city):
    lat, lon, loc_name = get_coords(city)
    weather_url = (f'https://api.openweathermap.org/data/2.5/'
                   +f'weather?lat={lat}&lon={lon}&appid={API}')
    response = requests.get(weather_url)
    inf = json.loads(response.text)
    weather_inf = (inf['weather'][0]['main']+'('
                   +inf['weather'][0]['description']+')')
    temp_inf = int(inf['main']['temp'])-273
    humidity_inf = int(inf['main']['humidity'])
    press_inf = int(inf['main']['pressure'])
    return weather_inf,temp_inf,humidity_inf,press_inf,loc_name


wether,temp,hum,press, city = get_weather(city_name)
print(f'В городе {city}: {wether}. '
      + f'Температура - {temp} °С, влажность - {hum} %, '
      +f'давление - {press}00 Па')
