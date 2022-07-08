from application import app, db
from flask import Flask, request, render_template, url_for
from application.models import Houses
import requests
from datetime import date


@app.route('/', methods = ['GET'])
def home():
    house_location = requests.get('http://houselocation:5000/get_location').text
    house_size = requests.get('http://housesize:5000/get_size').text
    price = requests.post('http://houseprice:5000/get_price', json = {"Location": house_location, "Size": house_size}).text
    #print(" MY Output Lines:")
    #print(house_location)
    #print(house_size)
    #print(price)
    house = Houses(house_location = house_location, house_size = int(house_size), house_price = int(price), date_generated = date.today())
    db.session.add(house)
    #print("Added to DB")
    db.session.commit()
    #print("Committed to DB")
    #past5 = Events.query.order_by(Events.id.desc()).limit(5).all()
    return render_template('index.html', house = house)