from application import app
from flask import Flask, request, Response
import random

@app.route('/get_location', methods=['GET'])
def location():
    house_location = random.choice(["Beverly Hills", "Vegas Strip", "Mayfair","Bay Area", "Paris", "Barcelona"])
    return Response(house_location, mimetype='text/plain')