

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
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
import json
import os, time, random
from giveaway import Giveaway
from flask_socketio import SocketIO, emit
import json
async_mode = None
socketio = SocketIO(app, async_mode=async_mode)
thread = None


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
import requests		
from random import randint




##################################################################################################################
#--------------------DECODE--------------------------------------------------------------------------------------#
##################################################################################################################


def background_thread():
    kisiler = 0

    socketio.sleep(2)


    (kisiler) =Giveaway(user,password,give_away_people).send_winners(user,password,postlink,max_limit)

    socketio.emit('my_response',
    {'data': 'Values', 'kisiler': kisiler},
    namespace='/kazananlar')




@socketio.on('connect', namespace='/kazananlar')
def test_connect():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')






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
            give_away_people = ['@jakobowsky', '@someone']
            templateData = {
                'mesg': mesg,
                'speed': speed
            }

            winners=["Çekiliş yapılıyor..."]
            return render_template("cekilis.html", async_mode=socketio.async_mode, **templateData, winners=winners)


if __name__ == '__main__':
    HOST = environ.get('0.0.0.0', 'localhost')
    try:
        PORT = int(environ.get('80', '5000'))
    except ValueError:
        PORT = 80
    #Sinif().sinif()
    #app.run(HOST, PORT)
    socketio.run(app, debug=True)



##################################################################################################################
