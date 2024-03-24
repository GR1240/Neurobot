#  Необходимо установить расширение командой  pip install requests
import os
import datetime
import requests
WEATHER_API_KEY = '023a6a170c4ed97ffc94ab802fe5aa16'

def get_weather(city):
    url = (f"http://api.openweathermap.org/data/2.5/weather?q=москва&lang=ru&units=metric&appid=&appid={WEATHER_API_KEY}")
    response = requests.get(url).json()
    return response['main']['temp']
    
if __name__ == '__main__':
    get_weather()    
    
    
#     url = 'https://randomfox.ca/floof/'
#     # url = ''
#     response = requests.get(url)
#     if response.status_code:
#         data = response.json()
#         return data.get('image')


# if __name__ == '__main__':
#     weather()