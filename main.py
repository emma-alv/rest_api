from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
# from requests import get

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an Api'},
    'todo2': {'task': '????'}
}

STUDENT = {
    'originator':'Emmanuel'
}


class TodoList(Resource):
    def get(self):
        return TODOS


class StudentList(Resource):

    def get(self):
        return STUDENT

class Student(Resource):
    def get(self, student):
        return STUDENT[student]


api.add_resource(TodoList,'/todos')
api.add_resource(StudentList,'/student')
api.add_resource(Student,'/student/<student>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='12345')
