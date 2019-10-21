from flask import Flask
from flask_restful import Api , Resource


app = Flask(__name__)

api = Api(app)

class Item(Resource):
    def get(self, name):
        return {'student':name}

api.add_resource(Item,'/student/<string:name>')

app.run(port=5006)

