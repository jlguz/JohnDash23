import requests
import datetime, random

from django.shortcuts import render




def home(request):

      if request.method == 'POST':
            city = request.POST['city'].title()
            weather_date = my_weather(city)

            city_weather = {
                  'city': city,
                  'temperature': weather_date['main']['temp'],
                  'description' : weather_date['weather'][0]['description'],
                  'icon': weather_date['weather'][0]['icon'],
                  'country': weather_date['sys']['country'],
                        }
            
            context = {'city_weather': city_weather, }
            return render(request, 'home/index.html', context)
      else:
            return render(request, 'home/index.html')
      



def weather(request):

      if request.method == 'POST':


            city = request.POST['city'].title()
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=e65aeb7bf4726c253e4e01990fee472a'
            r = requests.get(url).json()
            
            if r['cod'] == 200:
                  city_weather = {
                                    'city': city,
                                    'temperature': r['main']['temp'],
                                    'description' : r['weather'][0]['description'],
                                    'icon': r['weather'][0]['icon'],
                                    'country': r['sys']['country'],
                                    
                              }
                  print(r)
                  context = {'city_weather' : city_weather,}

                  return render(request, 'home/weather.html', context)
            else:
                  city_weather = {}
                  context = {'city_weather': city_weather, }
                  return render(request, 'home/weather.html', context)



def my_weather(city):

      url = 'https://api.openweathermap.org/data/2.5/weather?units=metric&appid=e65aeb7bf4726c253e4e01990fee472a'

      parameter = {
            'q': city,
      }

      response = requests.get(url, params=parameter).json()

      if response['cod'] == 200:
            return response
      else:
            return None


def lottery():
      lotto = list(range(1, 60))


      lotto_numbers = random.sample(lotto, k=6)
      print(lotto_numbers)


      euro = list(range(1, 51))
      starts = list(range(1, 13))

      euro_numbers = random.sample(euro, k=5)
      euro_starts = random.sample(starts, k=2)

      euromillions = f"{euro_numbers}{euro_starts}"

      print(euromillions)
      