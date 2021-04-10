from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import models.orders as orders
import os

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.route('/')
def Getorders():
    all_orders = orders.orders.query.all()
    print(all_orders)
    return jsonify({'orders':all_orders})

@app.route('/api/addOrder', methods=['GET', 'POST'])
def addOrder():
    """Create a user via query string parameters."""
    content = request.json
    print(content)

    data = request.args.get('OBJ')
    print(data)
    if data:
        existing_order = orders.query.filter(
            orders.ORDER_ID == data[0] 
        ).first()
        if existing_order:
            return  {'message': "orderID exist"}, 500
        new_order = orders(db)  # Create an instance of the User class
        db.session.add(new_order)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return  {'message': "successful"}, 200
    else:  {'message': "unsuccesful"}, 500



def main():
   db.create_all()
   app.run()
if __name__ == "__main__":
    with app.app_context():
        main()