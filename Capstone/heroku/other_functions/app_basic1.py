# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 12:34:26 2019

@author: jnpicao
"""

# the request object does exactly what the name suggests: holds
# all of the contents of an HTTP request that someone is making
# the Flask object is for creating an HTTP server - you'll
# see this a few lines down.
# the jsonify function is useful for when we want to return
# json from the function we are using.

from flask import Flask, request, jsonify

# here we use the Flask constructor to create a new
# application that we can add routes to

app = Flask(__name__)
  

@app.route('/predict', methods=['POST'])
def predict():
    payload = request.get_json()
    at_risk = payload['unemployed']
    return jsonify({
        'prediction': at_risk
    })

if __name__ == "__main__":
    app.run(debug=True)