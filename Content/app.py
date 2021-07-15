from flask import Flask
from models import mongo

def create_app():
    app=Flask(__name__)

    app.config['MONGO_URI'] = 'mongodb+srv://abhinav:Password@10@cluster0.axu85.mongodb.net/To_Do_App?retryWrites=true&w=majority'

    mongo.init_app(app)
    return app

