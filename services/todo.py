import os
from bson.objectid import ObjectId
from pymongo import MongoClient

mongodb_uri = os.getenv('MONGODB_URI', 'mongodb://localhost/')
db_name = os.getenv('DB_NAME', 'todos')

client = MongoClient(mongodb_uri)
db = client[db_name]
todos = db['todos']


def create_todo(data):
    todos.insert_one(data)


def update_todo(todo_id, data):
    todo = todos.find_one_and_update({'_id': ObjectId(todo_id)}, {'$set': data}, return_document=True)
    return todo


def delete_todo(todo_id):
    todos.find_one_and_delete({'_id': ObjectId(todo_id)})


def get_todos(conditions):
    if '_id' in conditions:
        conditions['_id'] = ObjectId(conditions['_id'])
    results = todos.find(conditions)
    todos_data = []
    for data in results:
        todos_data.append(dict(data))
    return todos_data
