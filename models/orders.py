from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'orders'

    ORDER_ID = db.Column(db.Integer, primary_key=True)
    CUSTOMER_ID = db.Column(db.Integer)
    ORDER_DATE = db.Column(db.DateTime)
    SHIPPING_DATE = db.Column(db.DateTime)
    PRODUCT_ID = db.Column(db.Integer)
    PRODUCT_NAME = db.Column(db.String)
    PRODUCT_CATEGORY = db.Column(db.String)
    NAME = db.Column(db.String)
    GENDER = db.Column(db.String)
    STREET_ADDRESS = db.Column(db.String)
    CITY = db.Column(db.String)
    STATE = db.Column(db.String)
    POSTAL_CODE = db.Column(db.Integer)
    COUNTRY = db.Column(db.String)
    YEAR_OF_BIRTH = db.Column(db.Integer)
    DESCRIPTION = db.Column(db.String)
    DATA_COLLECTED = db.Column(db.String)

    

    def __init__(self, obj):
        self.ORDER_ID = obj[0]
        self.CUSTOMER_ID = obj[1]
        self.ORDER_DATE = obj[2]
        self.SHIPPING_DATE = obj[3]
        
        self.PRODUCT_ID = obj[4]
        self.PRODUCT_NAME= obj[5] 
        self.PRODUCT_CATEGORY = obj[6]
        self.NAME = obj[7]
        self.GENDER = obj[8]
        
        self.STREET_ADDRESS = obj[9]
        self.CITY = obj[10]
        self. STATE = obj[11]
        self.POSTAL_CODE = obj[12]
        self.COUNTRY = obj[13]
        YEAR_OF_BIRTH= obj[14]
        self.DESCRIPTION = obj[15]
        self.DATA_COLLECTED = obj[16]

    def __repr__(self):
        return '<id {}>'.format(self.id)