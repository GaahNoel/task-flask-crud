import pytest
import requests

BASE_URL = "http://localhost:5000"
created_task_id = None
tasks = []

def test_create_task(): 
  data = {
    "title": "New task",
    "description": "Any new task"
  }

  response = requests.post(f'{BASE_URL}/tasks', json=data)
  response_data = response.json()

  tasks.append(response_data["id"])

  assert response.status_code == 200
  assert "id" in response_data
  

def test_get_tasks():
  response = requests.get(f'{BASE_URL}/tasks') 
  response_data = response.json()
  assert response_data["length"] > 0
  assert len(response_data["tasks"]) > 0

def test_get_task(): 
  created_task_id = tasks[0]
  response = requests.get(f'{BASE_URL}/tasks/{created_task_id}') 
  response_data = response.json()
  assert response.status_code == 200
  assert response_data["id"] == created_task_id

def test_update_task(): 
  data = {
    "title": "New task",
    "description": "Any new description",
    "completed": True
  }

  created_task_id = tasks[0]
  response = requests.put(f'{BASE_URL}/tasks/{created_task_id}', json=data) 
  response_data = response.json()

  assert response.status_code == 200
  assert response_data["id"] == created_task_id
  assert response_data["completed"] == True
  assert response_data["description"] == "Any new description"

def test_delete_task(): 
  created_task_id = tasks[0]
  response = requests.delete(f'{BASE_URL}/tasks/{created_task_id}') 
  assert response.status_code == 200

  get_response = requests.get(f'{BASE_URL}/tasks/{created_task_id}') 
  assert get_response.status_code == 404