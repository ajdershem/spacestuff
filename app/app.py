#!/usr/bin/env python3
from flask import Flask, render_template, jsonify
import requests
from flask_googlemaps import GoogleMaps
from datetime import datetime


app = Flask(__name__)
GoogleMaps(app)


@app.route('/')
def index():
    people = get_space_people()
    lat, lon = get_iss_location()

    return render_template("index.html", people=people,
                           iss_lat=lat, iss_lon=lon)


@app.route('/api/v1/issposition/<lat>/<lon>')
def get_iss_pass_time(lat, lon):
    base_url = 'http://api.open-notify.org/iss-pass.json?'
    url = base_url + "lat=" + lat + "&lon=" + lon
    response = requests.get(url)
    response = response.json()

    dates = datetime_to_tuple(response)

    return jsonify(dates=dates)


def datetime_to_tuple(response):
    list_o_dates = []

    for item in response['response']:
        date_time = datetime.fromtimestamp(item['risetime'])
        date = date_time.strftime("%b %d, %Y")
        time = date_time.strftime("%H:%M")
        list_o_dates.append({'date': date, 'time': time})

    return list_o_dates


def get_iss_location():
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    response = response.json()
    lat = response['iss_position']['latitude']
    lon = response['iss_position']['longitude']

    return (lat, lon)


def get_space_people():
    url = 'http://api.open-notify.org/astros.json'
    response = requests.get(url)
    response = response.json()

    return response['people']


if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
