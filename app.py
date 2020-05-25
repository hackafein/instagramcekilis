

"""
CoDeR= Hüseyin Furkan Ceran
"""
#-------iMPORTLAR---------------------------------------------------------------------------------------------------
import time
import os
import random
from os import environ
import sys
import urllib
from flask import Flask, redirect, render_template, request, url_for,flash
import json
import os, time, random
from giveaway import Giveaway



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
import requests		
from random import randint




##################################################################################################################
#--------------------DECODE--------------------------------------------------------------------------------------#
##################################################################################################################

@app.route("/")
def index():
    return render_template("index.html")
def about():
        return render_template("about.html")
@app.route("/exit", methods=['GET', 'POST'])
def exit():
        return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(500)
def server_error(e):
	return render_template('404.html'), 500


@app.route("/cekilis", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        if request.form["action"] == "giveaway":
            user = request.form.get("user")
            password = request.form.get("pass")
            postlink= request.form.get("postlink")
            max_limit = int(request.form.get("searching_limit"))

            winners=Giveaway.send_winners(user,password,postlink,max_limit)
            return render_template("cekilis.html", winners=winners)


if __name__ == '__main__':
    HOST = environ.get('0.0.0.0', 'localhost')
    try:
        PORT = int(environ.get('80', '5000'))
    except ValueError:
        PORT = 80
    #Sinif().sinif()
    app.run(HOST, PORT)



##################################################################################################################
