from flask import Flask
from flask_restful import Api , Resource


app = Flask(__name__)

api = Api(app)

students = []

class Item(Resource):
    def get(self, name):
        for student in students:
            if student['name'] == name:
                return student
        return {'Student': None}, 404

    
    def post(self, name):
        student = {'students':name, 'Fee':25000}
        students.append(student)
        return student, 201

api.add_resource(Item,'/student/<string:name>')

app.run(port=5022, debug=True)


