import datetime as dt
import requests

base_url="http://api.openweathermap.org/data/2.5/weather?"
api_key="e263cccc5432c61d0910221f2f37bab0"
location=input("Enter city name: ")

url=base_url+"&q="+location+"&appid="+api_key
response=requests.get(url).json()

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius=kelvin-273.15
    fahrenheit=celsius*(9/5)+32
    return celsius,fahrenheit

temp_kelvin=response['main']['temp']
temp_celsius,temp_fahrenheit=kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin=response['main']['feels_like']
feels_like_celsius,feels_like_fahrenheit=kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed=response['wind']['speed']
humidity=response['main']['humidity']
description=response['weather'][0]['description']
sunrise_time=dt.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
sunset_time=dt.datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])

print(f"Temperature in {location}:{temp_celsius:.2f}C or {temp_fahrenheit:.2f}F")
print(f"Temperature in {location} feels like:{feels_like_celsius:.2f}C or {feels_like_fahrenheit:.2f}F")
print(f"Humidity in {location}: {humidity}%")
print(f"Wind Speed in {location}: {wind_speed}m/s")
print(f"General Weather in {location}: {description}")
print(f"Sun rises in {location} at {sunrise_time} local time")
print(f"Sun sets in {location} at {sunset_time} local time")
