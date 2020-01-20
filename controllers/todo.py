from flask import Blueprint, render_template, request

from utils.api import response, error_response, validate_body
from services.todo import create_todo, get_todos, update_todo, delete_todo

todo = Blueprint('todo', __name__)


@todo.route('/')
def display_todos():
    return render_template('todos.html')


@todo.route('/', methods=['POST'])
def create():
    body = request.get_json()
    status, missing_field = validate_body(body, ['task'])
    if not status:
        return error_response(f'{missing_field} is required')
    try:
        create_todo(body)
        return response(True, 'Todo created successfully', body)
    except Exception as err:
        print('=====> Error', err)
        return error_response(str(err))


@todo.route('/', methods=['GET'])
def view():
    conditions = dict(request.args)
    try:
        data = get_todos(conditions)
        return response(True, 'Todo List', data)
    except Exception as err:
        print(f'=====> Error', err)
        return error_response(str(err))


@todo.route('/<todo_id>', methods=['PUT'])
def update(todo_id):
    body = request.get_json()
    try:
        todo_task = update_todo(todo_id, body)
        return response(True, 'Todo task updated successfully', todo_task)
    except Exception as err:
        print(f'=====> Error', err)
        return error_response(str(err))


@todo.route('/<todo_id>', methods=['DELETE'])
def delete(todo_id):
    try:
        delete_todo(todo_id)
        return response(True, 'Todo task deleted successfully', None)
    except Exception as err:
        print(f'=====> Error', err)
        return error_response(str(err))
