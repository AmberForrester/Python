from flask import Flask, render_template, request
from forecast import get_my_weather, get_weather_by_coordinates

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/weather")
def get_weather():
    city = request.args.get("city")
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    weather_data = None

    if city:
        weather_data = get_my_weather(city)
    elif lat and lon:
        weather_data = get_weather_by_coordinates(lat, lon)
    
    if weather_data and weather_data.get("cod") == 200:
        return render_template(
            "weather.html",
            title=weather_data.get("name", "Unknown Location"),
            status=weather_data["weather"][0]["description"].capitalize(),
            temp=f"{weather_data['main']['temp']:.1f}",
            feels_like=f"{weather_data['main']['feels_like']:.1f}",
            country=weather_data["sys"]["country"],
        )
    else:
        error_message = "City not found or unable to retrieve location data."
        return render_template('index.html', error_message=error_message, city=city)

if __name__ == '__main__':
    app.run(debug=True)