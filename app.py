from flask import Flask, abort, render_template
import json
#import os
app=Flask(__name__)

with open("MSX.json") as fichero:
    datos=json.load(fichero)

@app.route('/', methods=["GET"])
def inicio():
    return render_template('inicio.html')

app.run('0.0.0.0', debug=True)