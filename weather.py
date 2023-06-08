import json
import requests

API_KEY="918713575dff83f79a7ac9309a272f9c"

def get_weather(lat,lon):
    url= "https://api.openweathermap.org/data/2.5/weather?&lat="+lat+"&lon"+lon+"&appod="+API_KEY
    response=requests.get(url)
    response_json=response.json()
    return response_json


def kelvin_to_F(k):
    return (k-273.15)*9/5+32

def kelvin_to_c(k):
    return k-273.15
temp=get_weather('43.605366','3.881346')
kelvin_to_F(temp)
