from flask_restful import Resource
from Models.store_model import storeModel

class Store(Resource):
    def get(self, name):
        store=storeModel.find_by_name(name)
        if store:
            
            return store.json()
        return{'message':'Store not found'}
    
    def post(self, name):
        if storeModel.find_by_name(name):
            return{'messsage':"Store named '{}'already exists".format(name)}
        store=storeModel(name)
        try:
            store.save_to_database()
        except:
            return{'message':'An error occured while saving the store'}, 500
        return store.json()
    
    def delete(self,name):
        store=storeModel.find_by_name(name)
        if store:
            store.delete_from_database()
        return{'message':"Store named'{}' has been deleted" .format(name)}

    
class StoreList(Resource):
        def get(self):
            try:
              return{'stores':[store.json() for store in storeModel.query.all()]}
            except:
             return{'message':'Could not load stores'}
                
            
  