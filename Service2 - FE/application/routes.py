from application import app, db
from flask import Flask, request, render_template, url_for
from application.models import Houses
import requests
from datetime import date


@app.route('/', methods = ['GET'])
def home():
    house_location = requests.get('http://houselocation:5000/get_location')
    house_size = requests.get('http://housesize/get_size')
    price = requests.post('http://housepirce:5000/get_price', json = {"Location": size.text, "Size": size.Integer})
    house = Events(house_location = house_location.text, house_size = house_size.Integer, price = price.Integer, date_generated = date.today())
    db.session.add(house)
    db.session.commit()
    #past5 = Events.query.order_by(Events.id.desc()).limit(5).all()
    return render_template('index.html', house = house''' , past5 = past5''')