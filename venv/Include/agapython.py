#SENTENCIA PARA ACTIVAR VIRTUAL ENVIROMENT: cmd y luego venv\Scripts\activate
from flask import Flask, jsonify, abort
from flask import make_response
from flask import request
import pandas as pd
import usuarioController
app = Flask(__name__)

contUsuario = usuarioController.controlador()
#Metodo de retorno de las Asignaciones
@app.route('/agapython/listarUsuarios', methods=['GET'])
def get_Usuarios():
    return jsonify(contUsuario.listarUsuarios())

#Metodo de retorno de las Asignaciones
@app.route('/agapython/insertarUsuarios', methods=['POST'])
def insert_Usuarios():
    name = request.form['Nombre']
    lastname = request.form['Apellido']
    contUsuario.insertarUsuario(name,lastname)
    return jsonify({'Success'})
    
#Metodo de mapeo de errores
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
#Creacion de tarea daemon que ejecute el algoritmo de asignacion de vuelos cada 15 segundos
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
