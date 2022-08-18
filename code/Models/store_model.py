from database import db

class storeModel(db.Model):

    __tablename__= "stores"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80))
    
    items=db.relationship('itemModel', lazy='dynamic')
    def __init__(self, name):
        self.name=name

    def json(self):
        return{'name': self.name, 'items': [items.json() for items in self.items.all]}

    @classmethod   
    def find_by_name(cls,name):
      return cls.query.filter_by(name=name).first()
    
   #this method inserts and updates too
    def save_to_database(self):
       db.session.add(self)
       db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit() 