from flask import Flask, abort, render_template, request
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

@app.route('/listajuegos', methods=["POST"])
def listajuegos():
    nombre_juego=request.form.get("nombre")
    lista_nombres=[]
    lista_desarrolladores=[]
    for juegos in datos:
        if str(juegos["nombre"]).startswith(nombre_juego):
            lista_desarrolladores.append(juegos["desarrollador"])
            lista_nombres.append(juegos["nombre"])
    return render_template("listajuegos.html", lista_nombres=lista_nombres, lista_desarrolladores=lista_desarrolladores)

app.run('0.0.0.0', debug=True)