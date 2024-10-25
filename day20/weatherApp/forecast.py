from dotenv import load_dotenv
import requests
import os

load_dotenv()

def get_my_weather(city):
    api_key = os.getenv("API_KEY")
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=metric"
    response = requests.get(request_url)
    weather_data = response.json()
    return weather_data

def get_weather_by_coordinates(lat, lon):
    api_key = os.getenv("API_KEY")
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&lat={lat}&lon={lon}&units=metric"
    response = requests.get(request_url)
    weather_data = response.json()
    return weather_data

if __name__ == "__main__":
    print("Weather by City")
    city_weather = get_my_weather("new york")
    print(city_weather)

    print("\nWeather by Coordinates")
    coord_weather = get_weather_by_coordinates(40.7128, -74.0060)
    print(coord_weather)
