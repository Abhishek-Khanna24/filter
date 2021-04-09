from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import os

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://cvwyupld:3Fu0SAYQdkB0f6JWbSpLIn632Y4JQWn9@queenie.db.elephantsql.com:5432/cvwyupld"
db = SQLAlchemy(app)

from models import orders


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>', methods=['GET'])
def user_records():
    """Create a user via query string parameters."""
    data = request.args.get('OBJ')
    if data:
        existing_order = orders.query.filter(
            orders.ORDER_ID == data[0] 
        ).first()
        if existing_order:
            return make_response(
                f'{data[0]} ({data[1]}) already created!'
            )
        new_order = orders(db)  # Create an instance of the User class
        db.session.add(new_order)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return  {'message': "successful"}, 200
    else:  {'message': "unsuccesful"}, 500

if __name__ == '__main__':
    app.run()