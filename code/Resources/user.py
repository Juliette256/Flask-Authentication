
import sqlite3
from flask_restful import Resource, reqparse

from Models.user_model import UserModel

class RegisterUser(Resource):
 parser=reqparse.RequestParser()
 parser.add_argument('username', type=str, required=True, help="Can not be empty")
 parser.add_argument('password', type=str, required=True, help="Can not be empty")
    
 def post(self):
     data=RegisterUser.parser.parse_args()
     if UserModel.find_by_username(data['username']):
         return {"message":"Already exists"},400

     connection=sqlite3.connect('data.db')
     cursor=connection.cursor()

     query="INSERT INTO users VALUES(NULL, ?, ?)"
     cursor.execute(query, (data['username'], data['password']))

     connection.commit()
     connection.close()
     return {"message":"User has been registered successfully"} ,201
