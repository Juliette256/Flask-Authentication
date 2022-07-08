
from flask import Flask, request
from flask_restful import Resource, Api,reqparse
from flask_jwt import JWT,jwt_required

from security import authenticate, identity
from user import RegisterUser
from item import Item,ItemList

app=Flask(__name__)
app.secret_key='jose'
api=Api(app)

jwt=JWT(app,authenticate,identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(RegisterUser, '/register')

app.run(port=5000, debug=True)
