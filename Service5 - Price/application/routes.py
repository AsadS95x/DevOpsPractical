from application import app
from flask import Flask, request, Response

@app.route('/get_price', methods = ['POST'])
def price():
    house_data = request.get_json()
    house_location = house_data["Location"]
    house_size = house_data["Size"]
    #house_size= int(hs)
    print ("house_size: "+ str(house_size))
    #print(" Why is this not showing..... "+ hs)
    size_cost = {"1": 100000}
    if int(house_size) >1:
        np=int(house_size)*size_cost["1"]
        size_cost.update({house_size: np}) 
    location_cost = {"Beverly Hills": 3, "Vegas Strip": 2, "Mayfair": 6,"Bay Area": 5, "Paris": 3, "Barcelona": 1}
    price = location_cost[house_location]*size_cost[house_size]
    return Response(str(price), mimetype='text/plain')