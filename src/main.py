"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify
from models import db, Task #,User
#from models import Person

app = Flask(__name__)
#mysql+pymysql://flask4p1:123321...@85.10.205.173:3306/flaskapi
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://yraidaguillen:superadmin...@85.10.205.173:3306/yg_todolist"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# generate sitemap with all your endpoints
@app.route('/') #Esto es un decorador
def home():
    return jsonify({"mensaje":"Bienvenidos a mi app"})

#@app.route('/tareas', methods=['GET','PUT'])
#def obtener_tareas():
#    if request.method == 'GET':
#        return jsonify({"mensaje_via_get":"Bienvenidos a mi app GET"})
#    if request.method == 'PUT':
#        return jsonify({"mensaje_via_put":"Bienvenidos a mi app PUT"})


@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    tasks = Task.query.all() # Nos taremos la lista de tareas, nos va a traer una lista de clases
    print(tasks)
    allTasks = [task.serialize() for task in tasks] #task individual de cada lista que viene de BD task.serialize va a convertir la tarea a formato json
    return jsonify({"mensaje": "Bienvenido a mi app GET", "tasks": allTasks})

@app.route('/tareas/<id>', methods=['GET'])
def obtener_detalle_tareas(id):
    task_found = Task.query.get(id)
    if not task_found:
        return jsonify({ "mensaje": 'tarea no encontrada', "task": {}})
    return jsonify({ "mensaje": 'tarea obtenida satisfactoriamente', "task": task_found.serialize()})
    

@app.route('/tareas', methods=['POST'])
def agregar_tareas_post():
    name = request.json["name"]
    done = request.json["done"]
    new_task = Task(name = name, done = done)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"mensaje":"Bienvenidos a mi app POST", "task": new_task.serialize()})

@app.route('/tareas/<id>', methods=['PUT'])
def actualizar_tareas(id):
    task_found = Task.query.get(id)
    if not task_found:
        return jsonify({ "mensaje": 'tarea no encontrada', "task": {}})
    task_found.name = request.json["name"]
    task_found.done = request.json["done"]
    db.session.commit()
    return jsonify({ "mensaje": 'tarea actualizada satisfactoriamente', "task": task_found.serialize()})
    

@app.route('/tareas/<id>', methods=['DELETE'])
def obtener_tareas_delete(id):
    if not task_found:
        return jsonify({ "mensaje": 'tarea no encontrada', "task": {}})
    db.session.delete(task_found)
    db.session.commit()
    return jsonify({ "mensaje": 'tarea eliminada satisfactoriamente', "task": task_found.serialize()})

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__': 
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True) # es la que levanta el servidor
