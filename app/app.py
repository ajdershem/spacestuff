#!/usr/bin/env python3

from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/')
def index():
    people = get_space_people()
    return render_template("index.html", people=people)


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
    app.run()
