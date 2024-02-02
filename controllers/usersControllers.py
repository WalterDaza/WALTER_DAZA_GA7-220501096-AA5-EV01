from models.usersModels import registroUsuariosModel, loginUsuarioModel
from flask import jsonify #libreria para formatos json


#Registrar Usuarios***********************************************
def crearUsuariosControllers(datos):
    result = [str(registroUsuariosModel(datos))] #se pasa la respuesta (boolean) a texto con str
    return jsonify(result)#se convierte a formato json


#Login Usuarios****************************************************
def loginUsuariosController(datos):
    result = (loginUsuarioModel(datos))

    if result:
        return ("Sesión Iniciada") #Si result tiene información se inicia sesión
        # return jsonify(result)
    else:
        return ("Credenciales invalidas")