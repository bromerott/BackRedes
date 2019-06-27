#SENTENCIA PARA ACTIVAR VIRTUAL ENVIROMENT: cmd y luego venv\Scripts\activate
from flask import Flask, jsonify, abort
from flask import make_response
from flask import request
import pandas as pd
app = Flask(__name__)

#Base de Datos de Usuarios
dfUsuarios = pd.DataFrame(columns={'Nombre','Apellido'})
dfUsuarios = dfUsuarios.append({'Nombre' : 'Bruno' , 'Apellido' : 'Romero'} , ignore_index=True)
dfUsuarios = dfUsuarios.append({'Nombre' : 'Sebastian' , 'Apellido' : 'Villa-Garcia'} , ignore_index=True)

#Metodo de retorno de las Asignaciones
@app.route('/agapython/listarUsuarios', methods=['GET'])
def get_Asignaciones():
    return jsonify({dfUsuarios.to_json(orient='records')})
    
#Metodo de mapeo de errores
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
#Creacion de tarea daemon que ejecute el algoritmo de asignacion de vuelos cada 15 segundos
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
