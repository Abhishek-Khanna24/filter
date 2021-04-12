from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import models.orders as orders
import os
from datetime import datetime
from sqlalchemy import func


app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'
db = SQLAlchemy(app)

@app.route('/orders', methods=['GET', 'POST'])
def all_orders():
    if request.method == 'GET':
        all_orders = orders.orders.query.all()
        return jsonify(all_orders)
    elif request.method == 'POST':
        data = request.get_json()
        print(data)
        new_order = orders.orders(data)
        db.session.add(new_order)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return  jsonify(new_order), 200

@app.route('/orders/<order_id>', methods=['GET', 'DELETE', 'PUT'])
def get_order(order_id):
    if request.method == 'GET':
        all_orders = orders.orders.query.filter_by(order_id=order_id)
        return jsonify(all_orders[0])
    elif request.method == 'DELETE':
        orders.orders.query.filter_by(order_id=order_id).delete()
        db.session.commit()
        return {'message': 'delete successful'}, 204
    elif request.method == 'PUT':
        data = request.get_json()
        orders.orders.query.filter_by(order_id=order_id).update(data)
        db.session.commit()
        return {'message': 'update successful'}, 200
    

@app.route('/dashboard')
def get_dashboard():
    res = {}

    check_date = datetime.strptime("2017", '%Y')
    data = orders.orders.query.filter(orders.orders.order_date>check_date).all()
    res['vis1'] = len(data)

    data = db.session.query(orders.orders.name, orders.orders.country, func.count(orders.orders.order_id)
            ).group_by(orders.orders.name, orders.orders.country).order_by(
                func.count(orders.orders.order_id).desc()).all()[:10]
    res['vis2'] = [{'name':x[0], 'country':x[1], 'count':x[2]} for x in data]

    data = db.session.query(orders.orders.data_collected, func.extract("month", orders.orders.order_date), func.count(orders.orders.order_id)).group_by(
        orders.orders.data_collected, func.extract("month", orders.orders.order_date)).all()
    res['vis3'] = [{'company':x[0], 'month':int(x[1]), 'count':x[2]} for x in data]
    return jsonify(res)

def main():
   db.create_all()
   app.run(port=3001)

if __name__ == "__main__":
    with app.app_context():
        main()