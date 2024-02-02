from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

from controllers.usersControllers import crearUsuariosControllers, loginUsuariosController #importación de controladores

app = Flask(__name__) #instaciamiento
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'

#Registro usuarios****************************************
@app.route('/api/registro', methods = ["POST"])
@cross_origin()

def createUser(): #información que se solicita al usuario en formato JSON
    datos = [
        request.json['usuario'],
        request.json['contrasena']
    ]
    if crearUsuariosControllers(datos): #controlador hace la petición
        return ("Usuario registrado exitosamente")
    else:
        return("Validar información, petición de registro denegada")

#Login Usuarios************************************************
@app.route('/api/login', methods=["POST"])
@cross_origin()

def loginUser(): #información que se solicita al usuario en formato JSON
    datos = [
        request.json['usuario'],
        request.json['contrasena']
    ]

    result = loginUsuariosController(datos)
    return result

#pagina por defecto
@app.route("/")
@cross_origin()

def index():
    return "Evidencia GA7-220501096-AA5-EV01 Walter Eduardo Daza Romero"


if __name__ == '__main__':
    app.run(port  = 3010, debug = True)