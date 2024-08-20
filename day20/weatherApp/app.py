from flask import Flask, render_template, request, url_for
from forecast import get_my_weather

app = Flask(__name__)



@app.route("/") # Default route 
def index():
    return render_template('index.html')

@app.route("/weather")
def get_weather():
    # city = "toronto"
    city = request.args.get("city")

    weather_data = get_my_weather(city)
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        country=weather_data["sys"]["country"],
    )



if __name__ == '__main__':
    
    app.run(debug=True) # Development mode not production to show errors. 