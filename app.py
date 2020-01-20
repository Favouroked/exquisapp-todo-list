from flask import Flask

from controllers.todo_api import todo_api

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


app.register_blueprint(todo_api, url_prefix='/api/todos')

if __name__ == '__main__':
    app.run()
