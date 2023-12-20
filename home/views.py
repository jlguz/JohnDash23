import requests
import datetime, random

from django.shortcuts import render


    

def home(request):
            
     
      if request.method == 'POST':

            city = request.POST['city'].title()
            weather_date = my_weather(city)

            if weather_date is None:

                  city = 'london'
                  weather_date = my_weather(city)

                  city_weather = {
                        'city': city,
                        'temperature': round(weather_date['main']['temp']),
                        'description': weather_date['weather'][0]['description'],
                        'icon': weather_date['weather'][0]['icon'],
                        'country': weather_date['sys']['country'],
                        'dt': datetime.datetime.fromtimestamp(weather_date['dt']),
                        }
                  
                  print(weather_date)

                  context = {'city_weather': city_weather, }

                  return render(request, 'home/index.html', context)
            


            
            if weather_date is not None:
                  city_weather = {
                        'city': city,
                        'temperature': round(weather_date['main']['temp']),
                        'description': weather_date['weather'][0]['description'],
                        'icon': weather_date['weather'][0]['icon'],
                        'country': weather_date['sys']['country'],
                        'dt': datetime.datetime.fromtimestamp(weather_date['dt']),
                        }
                  
                  print(weather_date)

                  context = {'city_weather': city_weather, }

                  return render(request, 'home/index.html', context)


      if request:


            city = 'london'
            weather_date = my_weather(city)

            city_weather = {
                  'city': city,
                  'temperature': round(weather_date['main']['temp']),
                  'description': weather_date['weather'][0]['description'],
                        'icon': weather_date['weather'][0]['icon'],
                        'country': weather_date['sys']['country'],
                        'dt': datetime.datetime.fromtimestamp(weather_date['dt']),
                  }
            
            context = {'city_weather': city_weather, }

            return render(request, 'home/index.html', context)
            
      return render(request, 'home/index.html')



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


def lottery(request):
            
      city = 'london'
      weather_date = my_weather(city)


      city_weather = {
                  'city': city,
                  'temperature': round(weather_date['main']['temp']),
                  'description': weather_date['weather'][0]['description'],
                        'icon': weather_date['weather'][0]['icon'],
                        'country': weather_date['sys']['country'],
                        'dt': datetime.datetime.fromtimestamp(weather_date['dt']),
                  }

      print(weather_date)

      lotto_num = list(range(1, 60))
      lotto = random.sample(lotto_num, k=6)
      print(lotto)


      euro_num = list(range(1, 51))
      starts = list(range(1, 13))

      euro_numbers = random.sample(euro_num, k=5)
      euro_starts = random.sample(starts, k=2)

      euromillions = f"{euro_numbers}{euro_starts}"

      print(euromillions)

      set_num = list(range(1, 51))
      life_num = list(range(1, 11))

      set_numbers = random.sample(set_num, k=5)
      life_starts = random.sample(life_num, k=1)

      setforlife = f'{set_numbers}{life_starts}'

      print(setforlife)

      lotto_numbers = {
                        'lotto': lotto,
                        'euro': euromillions,
                        'set' : setforlife
                  }

      context = {'lotto_numbers':lotto_numbers,
                  'city_weather': city_weather, }

      return render(request, 'home/lotto.html', context)
      

def lottery1():

      city = 'london'
      weather_date = my_weather(city)

      city_weather = {
            'city': city,
            'temperature': round(weather_date['main']['temp']),
            'description': weather_date['weather'][0]['description'],
            'icon': weather_date['weather'][0]['icon'],
            'country': weather_date['sys']['country'],
            'dt': datetime.datetime.fromtimestamp(weather_date['dt']),
      }

      print(weather_date)

      lotto_num = list(range(1, 60))
      lotto = random.sample(lotto_num, k=6)
      print(lotto)

      euro_num = list(range(1, 51))
      starts = list(range(1, 13))

      euro_numbers = random.sample(euro_num, k=5)
      euro_starts = random.sample(starts, k=2)

      euromillions = f"{euro_numbers}{euro_starts}"

      print(euromillions)

      set_num = list(range(1, 51))
      life_num = list(range(1, 11))

      set_numbers = random.sample(set_num, k=5)
      life_starts = random.sample(life_num, k=1)

      setforlife = f'{set_numbers}{life_starts}'

      print(setforlife)

      lotto_numbers = {
            'lotto': lotto,
            'euro': euromillions,
            'set': setforlife
      }

      context = {'lotto_numbers': lotto_numbers,
                  'city_weather': city_weather, }

      return render('home/index.html', context)





      






