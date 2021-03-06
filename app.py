import os

from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from security import authenticate, identity
from modelos.user import UserModel
from recursos.item import Item, ItemList
from recursos.users import UserRegister
from recursos.store import Store, StoreList
from db import db

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///data.db')
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres://tdtiotsbrwapba:3dacb2d534a83c56f31f4fc09d02e6038775e288e20ba322a772b5f16639e479@ec2-18-234-17-166.compute-1.amazonaws.com:5432/dcb4u9o8hoq9f1')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app) #facilita la creación de resoruces



db.init_app(app)
jwt = JWT(app, authenticate, identity) #Esto crea un endpoint nuevo, /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

#if __name__ == '__main__':
