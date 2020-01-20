from flask import Blueprint, render_template

todo = Blueprint('todo', __name__)


@todo.route('/')
def display_todos():
    return render_template('todos.html')
