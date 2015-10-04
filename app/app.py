#!/usr/bin/env python3

from flask import Flask, render_template, jsonify
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

#    $.getJSON('http://api.open-notify.org/iss-pass.json?lat=45.0&lon=-122.3&alt=20&n=5&callback=?', function(data) {
#            data['response'].forEach(function (d) {
#                        var date = new Date(d['risetime']*1000);
#                                 $('#isspass').append('<li>' + date.toString() + '</li>');
#                                     });
#            });


@app.route('/api/v1/issposition/<lat>/<lon>')
def get_iss_pass_time(lat, lon):
    base_url = 'http://api.open-notify.org/iss-pass.json?'
    url = base_url + "lat=" + lat + "&lon=" + lon #+ "&alt=20&n=5&callback=?"
    #url = 'http://api.open-notify.org/astros.json'
    response = requests.get(url)
    response = response.json()
    return jsonify(response)


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
