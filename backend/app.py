from flask import Flask
from flask_cors import CORS
from .extensions import db


def create_app():
  app= Flask(__name__)
  CORS(app, origins="*")
  return app

app= create_app()
db.init_app(app)


if __name__== "__main__":
  app.run(debug=True)