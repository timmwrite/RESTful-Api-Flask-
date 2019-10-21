from flask import Flask, request
from flask_restful import Api , Resource


app = Flask(__name__)

api = Api(app)

students = []

class Item(Resource):
    def get(self, name):
        student = filter(lambda x: x['name'==name, students])
        return {'Student': None}, 404

    
    def post(self, name):
        #data = request.get_json()
        student = {'students':name, 'fee': 25000}
        students.append(student)
        return student, 201

api.add_resource(Item,'/student/<string:name>')

app.run(port=5001, debug=True)


