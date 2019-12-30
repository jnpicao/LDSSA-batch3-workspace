# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 12:34:26 2019

@author: jnpicao
"""

# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!\n'

if __name__ == '__main__':
    app.run()
    
