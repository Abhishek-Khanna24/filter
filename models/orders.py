from dataclasses import dataclass
from app import db

from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.inspection import inspect

class Serializer(object):
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

@dataclass
class orders(db.Model):
    __tablename__ = 'orders'
    order_id : int
    customer_id : int
    order_date : str
    shipping_date : str
    product_id : int
    product_name : str
    product_category : str
    name : str
    gender : str
    street_address : str
    city : str
    state : str
    postal_code : int
    country : str
    year_of_birth : int
    description : str
    data_collected : str

    #id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer)
    order_date = db.Column(db.DateTime)
    shipping_date = db.Column(db.DateTime)
    product_id = db.Column(db.Integer)
    product_name = db.Column(db.String)
    product_category = db.Column(db.String)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    street_address = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    postal_code = db.Column(db.Integer)
    country = db.Column(db.String)
    year_of_birth = db.Column(db.Integer)
    description = db.Column(db.String)
    data_collected = db.Column(db.String)

    

    def __init__(self, obj):
        self.customer_id = obj['customer_id']
        self.order_date = obj['order_date']
        self.shipping_date = obj['shipping_date']
        self.product_id = obj['product_id']
        self.product_name= obj['product_name']
        self.product_category = obj['product_category']
        self.name = obj['name']
        self.gender = obj['gender']
        self.street_address = obj['street_address']
        self.city = obj['city']
        self. state = obj['state']
        self.postal_code = obj['postal_code']
        self.country = obj['country']
        self.year_of_birth= obj['year_of_birth']
        self.description = obj['description']
        self.data_collected = obj['data_collected']

    def __repr__(self):
        return '<id {}>'.format(self.order_id)

    def serialize(self):
        d = Serializer.serialize(self)
        del d['password']
        return d