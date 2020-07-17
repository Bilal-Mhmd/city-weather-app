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
    return render_template("city.html", city_name=name, data=r_json)


if __name__ == '__main__':
    app.run(debug=True)
