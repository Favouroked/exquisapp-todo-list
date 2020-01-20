from flask import render_template, Blueprint, request
from services.todo import create_todo

todo_client = Blueprint('todo_client', __name__)


@todo_client.route('/')
def render_view():
    return render_template('todos.html')

