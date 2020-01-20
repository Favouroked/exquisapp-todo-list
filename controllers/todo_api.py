from flask import Blueprint, render_template, request
from datetime import datetime

from utils.api import response, error_response, validate_body
from services.todo import create_todo, get_todos, update_todo, delete_todo

todo_api = Blueprint('todo_api', __name__)


@todo_api.route('/', methods=['POST'])
def create():
    body = {'task': request.form['task']}
    status, missing_field = validate_body(body, ['task'])
    if not status:
        return error_response(f'{missing_field} is required')
    try:
        data = {'task': body['task'], 'done': False, 'timeCreated': datetime.now()}
        create_todo(data)
        return response(True, 'Todo created successfully', data)
    except Exception as err:
        print('=====> Error', err)
        return error_response(str(err))


@todo_api.route('/', methods=['GET'])
def view():
    conditions = dict(request.args)
    try:
        data = get_todos(conditions)
        return response(True, 'Todo List', data)
    except Exception as err:
        print(f'=====> Error', err)
        return error_response(str(err))


@todo_api.route('/<todo_id>', methods=['PUT'])
def update(todo_id):
    body = {'done': request.form['done']}
    try:
        todo_task = update_todo(todo_id, body)
        return response(True, 'Todo task updated successfully', todo_task)
    except Exception as err:
        print(f'=====> Error', err)
        return error_response(str(err))


@todo_api.route('/<todo_id>', methods=['DELETE'])
def delete(todo_id):
    try:
        delete_todo(todo_id)
        return response(True, 'Todo task deleted successfully', None)
    except Exception as err:
        print(f'=====> Error', err)
        return error_response(str(err))
