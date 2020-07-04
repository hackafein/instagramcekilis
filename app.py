
import time
import os
import random
from os import environ
import sys
import urllib
from flask import Flask, redirect, render_template, request, url_for,flash, send_file, send_from_directory, safe_join, abort, jsonify
import json
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
import requests		
from random import randint
global longitude,latitude
longitude=0
latitude=0

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/menu", methods = ["GET", "POST"])
def menu():
    if request.method == "POST":	
        if request.form["action"] == "ceran":  

            if latitude==str(37.8817789) and longitude==str(32.505438):
                return render_template("shop.html")
            else:
                flash('Ceran Burger Lokasyonunda bulunamadığınız için Sisteme giriş yapamıyorsunuz')
                return redirect(url_for('index'))



@app.route('/_get_post_json/', methods=['POST','GET'])
def get_post_json():  
    if request.method == 'POST':
        data = request.get_json()
        datam=data.split("<br>")
        global longitude,latitude
        latitude=(datam[0])
        longitude=(datam[1])

        if latitude==str(37.8817789) and longitude==str(32.505438):
            print("Welcome Home Captain")

        return jsonify(status="success", data=data)









if __name__ == '__main__':
    HOST = environ.get('0.0.0.0', 'localhost')

    try:
        PORT = int(environ.get('80', '5000'))
    except ValueError:
        PORT = 80
    #Sinif().sinif()
    
    app.run(HOST, PORT)
    #socketio.run(app, debug=True)