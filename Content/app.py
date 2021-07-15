from flask import Flask
from models import mongo

def create_app():
    app=Flask(__name__)

    mongo.init_app(app)
    return app
mongodb+srv://abhinav:Password@10@cluster0.axu85.mongodb.net/To_Do_App?retryWrites=true&w=majority

@app.route("/")
def home():
    return "Pass Value"

@app.route("/<name>")              
def hello_name(name):             
    return "Hello "+ name 

if __name__ == "__main__":        
    app.run()
