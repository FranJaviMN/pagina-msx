from flask import Flask, abort, render_template
import json
#import os
app=Flask(__name__)

with open("MSX.json") as fichero:
    datos=json.load(fichero)

@app.route('/', methods=["GET"])
def inicio():
    return render_template('inicio.html')

@app.route('/juegos', methods=["GET", "POST"])
def juegos():
    return render_template('juegos.html')

app.run('0.0.0.0', debug=True)