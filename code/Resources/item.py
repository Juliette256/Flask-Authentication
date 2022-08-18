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
        try:
             item.save_to_database()
        except:
            return{'message':"An error occurred"}
        return item.json(), 201

    def delete(self,name):
        item=itemModel.find_by_name(name)
        if item:
            item.delete_from_database()
        return {'message':"Item deleted successfully"}
       

    def put(self, name):
    
        data=Item.parser.parse_args()
        item=itemModel.find_by_name(name)

        if item is None:
          item=itemModel(name, data['price'])
        else:
           item.price=data['price']  
        item.save_to_database()
             
        return item.json()
    

class ItemList(Resource):
    @jwt_required()
    def get(self):
    
     return{'items': list(map(lambda X:X.json(), itemModel.query.all()))}