import googlemaps
import pandas as pd
import requests

print("Welcome to weather API")
name = input("Please enter the city name")

gmaps = googlemaps.Client(key="AIzaSyAaGMWWFUVsFaIMcjo66vSts94ES0etG6I")
geocode_result = gmaps.geocode(name)

if not geocode_result:
    print("City not found!")
    exit()

r = geocode_result[0]
formatted_address = geocode_result[0]['formatted_address']
latitude = geocode_result[0]['geometry']['location']['lat']
longitude = geocode_result[0]['geometry']['location']['lng']
print(f"Location is: {formatted_address}")
print(f"Longitude of is: {longitude}")
print(f"Latitude is: {latitude}")

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
response = requests.get(url)
data = response.json()
print(f"Temperature currently is: {data["current"]["temperature_2m"]}{data["current_units"]['temperature_2m']}")