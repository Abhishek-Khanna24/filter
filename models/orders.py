from app import db
from sqlalchemy.dialects.postgresql import JSON


class orders(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
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
        self.order_id = obj[0]
        self.customer_id = obj[1]
        self.order_date = obj[2]
        self.shipping_date = obj[3]
        self.product_id = obj[4]
        self.product_name= obj[5] 
        self.product_category = obj[6]
        self.name = obj[7]
        self.gender = obj[8]
        self.street_address = obj[9]
        self.city = obj[10]
        self. state = obj[11]
        self.postal_code = obj[12]
        self.country = obj[13]
        self.year_of_birth= obj[14]
        self.description = obj[15]
        self.data_collected = obj[16]

    def __repr__(self):
        return '<id {}>'.format(self.order_id)