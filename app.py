import os
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)

api = Api(app)

Items = []

class Item(Resource):
    def get(self, name):
        for item in Items:
            if ['name'] == name:
                return item
            else:
                return{'Hey': None}, 404
                
    def post(self, name):
        item = {'student': name, 'price': 2000}
        Items.append(item)
        return item, 201
    
    


api.add_resource(Item,'/item/<string:name>')

if __name__ == '__main__':
    app.run(port=4000, debug=True)

    

