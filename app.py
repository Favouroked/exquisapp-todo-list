from flask import Flask

from controllers.todo import todo

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


app.register_blueprint(todo, url_prefix='/todos')

if __name__ == '__main__':
    app.run()
