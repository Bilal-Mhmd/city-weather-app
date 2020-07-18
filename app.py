from flask import Flask
from flask import render_template, request
import requests


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/city', methods=['POST'])
def weather():

    name = request.form['city']
    result = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={name}&appid=5e5ad119b5e3f33fbd99d1ebf3ca5db6')
    r_json = result.json()
    coord = r_json['coord']
    longitude_coord = coord['lon']
    latitude_coord = coord['lat']
    weather = r_json['weather'][0]['main']
    weather_description = str(r_json['weather'][0]['description']).capitalize()
    temp = format(float(r_json['main']['temp'] - 273.1), '.2f')
    pressure = r_json['main']['pressure']
    humidity = r_json['main']['humidity']
    return render_template("city.html", city_name=name, city_longitude=longitude_coord,
                           city_latitude=latitude_coord, city_weather=weather,
                           city_weather_descr=weather_description,
                           city_tempreture=temp, city_pressure=pressure,
                           city_humidity=humidity)


if __name__ == '__main__':
    app.run(debug=True)
