from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

from data import article

num1=100
num2=200
Articles=article()


## init app
app=Flask(__name__)

## creating a route
@app.route("/hello",methods=["GET"])
def get():
    return "Hello! Welcome To our Website"

@app.route("/Articles",methods=["GET"])
def article():
    return jsonify({"Data":Articles})


# Run Server
if __name__=="__main__":
    app.run(debug=True)








