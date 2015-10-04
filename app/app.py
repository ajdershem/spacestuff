#!/usr/bin/env python3

from flask import Flask, render_template
import requests
from flask_googlemaps import GoogleMaps


app = Flask(__name__)
GoogleMaps(app)


@app.route('/')
def index():
    people = get_space_people()
    iss_lat, iss_lon = get_iss_location()
    return render_template("index.html", people=people,
                           iss_lat=iss_lat, iss_lon=iss_lon)


def get_iss_location():
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    response = response.json()
    lat = response['iss_position']['latitude']
    lon = response['iss_position']['longitude']

    return (lat, lon)


def get_space_people():
    """
    {
      'number': 6,
      'people':
        [
          {
            'name': 'Mikhail Kornienko',
            'craft': 'ISS'
          },
          {'name': 'Scott Kelly', 'craft': 'ISS'},
          {'name': 'Oleg Kononenko', 'craft': 'ISS'},
          {'name': 'Kimiya Yui', 'craft': 'ISS'},
          {'name': 'Kjell Lindgren', 'craft': 'ISS'},
          {'name': 'Sergey Volkov', 'craft': 'ISS'}
          ],
      'message': 'success'
    }
    """
    response = requests.get('http://api.open-notify.org/astros.json')
    response = response.json()
    return response['people']

if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
