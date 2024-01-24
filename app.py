from flask import Flask, request, jsonify
from models.task import Task
from uuid import uuid4
app = Flask(__name__)

tasks = []

def list_tasks():
  return [task.to_dictionary() for task in tasks]

@app.route("/tasks", methods=["POST"])
def create_task():
  data = request.get_json()
  task = Task(uuid4(), data["title"], data["description"])
  tasks.append(task)
  return jsonify(task.to_dictionary())

@app.route("/tasks", methods=["GET"])
def get_tasks():
  tasks_list = list_tasks()
  return jsonify({
    "tasks": tasks_list,
    "length": len(tasks_list)
  })

@app.route("/tasks/<uuid:id>", methods=["GET"])
def get_task(id):
  find_task_condition = lambda t:t.id == id
  for task in tasks:
    if find_task_condition(task):
      return jsonify(task.to_dictionary())
  return jsonify("Not found"), 404


@app.route("/tasks/<uuid:id>", methods=["PUT"])
def update_task(id):
  find_task_condition = lambda t:t.id == id
  task = None
  for t in tasks:
    if find_task_condition(t):
      task = t
      break

  if task == None:
    return jsonify("Not found"), 404

  data = request.get_json()
  task.title = data["title"]
  task.description = data["description"]
  task.completed = data["completed"]

  return jsonify(task.to_dictionary())

@app.route("/tasks/<uuid:id>", methods=["DELETE"])
def delete_task(id):
  find_task_condition = lambda t:t.id == id
  task = None
  for t in tasks:
    if find_task_condition(t):
      task = t
      tasks.remove(t)
      break

  if task == None:
    return jsonify("Not found"), 404

  return jsonify(list_tasks())

if __name__=="__main__":
  app.run(debug=True)
