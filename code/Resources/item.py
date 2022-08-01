import json
import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from Models.item_model import itemModel

class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',
         type=float,
         required=True,
         help='This can not be empty')

    @jwt_required()
    def get(self, name):
        item =itemModel.find_by_name(name)
        if item:
         return item.json()
        return{"message":"Item not found"}, 404

    def post(self, name):
        if itemModel.find_by_name(name) : 
            return {'messsage':"An item with name'{}' already exists.".format(name)},400

        data=Item.parser.parse_args()
        item= itemModel(name, data['price'])
        item.insert()
        return item, 201

    def delete(self,name):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        query="DELETE FROM items WHERE name=?"
        cursor.execute(query,(name,))
        connection.commit()
        connection.close()
       
        return {'message':"Item has been deleted"}

    def put(self, name):
    
        data=Item.parser.parse_args()
        item=itemModel.find_by_name(name)
        updated_item= itemModel(name, data['price'])

        if item is None:
            # self.insert(updated_item)
            updated_item.insert()
        else:
        #   item.update(updated_item)
            updated_item.update()
        return updated_item.json()
    

class ItemList(Resource):
    @jwt_required()
    def get(name):
    
        connection =sqlite3.connect('data.db')
        cursor=connection.cursor()

        query="SELECT * FROM items" 
        result=cursor.execute(query,(name,))
        items=[]

        for row in result:
            items.append({'name':row[0], 'price':row[1]})
        connection.close()
        return{'items':items}