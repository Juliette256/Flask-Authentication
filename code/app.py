
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from Resources.user import RegisterUser
from Resources.item import Item,ItemList
from Resources.store import Store, StoreList

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='jose'
api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt=JWT(app,authenticate,identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/itemsList')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/storesList')
api.add_resource(RegisterUser, '/register')

if __name__ =='__main__':
    from database import db
    db.init_app(app)
    app.run(port=5000, debug=True)
