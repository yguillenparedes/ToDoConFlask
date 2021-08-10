"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify
from models import db, User
#from models import Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://yraidaguillen:superadmin...@85.10.205.173:3306/yg_todolist"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db.init_app(app)

# generate sitemap with all your endpoints
@app.route('/') #Esto es un decorador
def home():
    return jsonify({"mensaje":"Bienvenidos a mi app"})

@app.route('/tareas', methods=['GET','PUT'])
def obtener_tareas():
    if request.method == 'GET':
        return jsonify({"mensaje_via_get":"Bienvenidos a mi app GET"})
    if request.method == 'PUT':
        return jsonify({"mensaje_via_put":"Bienvenidos a mi app PUT"})

@app.route('/tareas', methods=['POST'])
def obtener_tareas_post():
    return jsonify({"mensaje_via_post":"Bienvenidos a mi app POST"})

#@app.route('/tareas', methods=['PUT'])
#def obtener_tareas_put():
    #return jsonify({"mensaje_via_put":"Bienvenidos a mi app PUT"})

@app.route('/tareas', methods=['DELETE'])
def obtener_tareas_delete():
    return jsonify({"mensaje_via_delete":"Bienvenidos a mi app DELETE"})

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
