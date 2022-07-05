from application import app
from flask import Flask, request, Response
import random

@app.route('/get_size', methods=['GET'])
def size():
    house_size = random.randrange(1,7)
    return Response(house_size, mimetype='text/plain')