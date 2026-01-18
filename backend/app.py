from flask import Flask
from flask_cors import CORS
from model import db, User, Role
from extensions import security
from config import LocalDevlopmentConfig
from dotenv import load_dotenv
from flask_security.datastore import  SQLAlchemyUserDatastore
## have to give a datastore when we init flask security in our app

load_dotenv()

def create_app():
  app= Flask(__name__)
  # for config
  app.config.from_object(LocalDevlopmentConfig)

  CORS(app, origins="*")

  # flask security staff
  datastore= SQLAlchemyUserDatastore(db, User, Role)
  security.init_app(app, datastore) # register_blueprint=False (will put this later;; first keep it's value default and go to /login end point you will see a default login page)
  # register_blue_print -> flask security has pre build endpoint for login and register;; error code etc;; we don't need bz we will have our own api

  app.datastore= datastore # pyright: ignore[reportAttributeAccessIssue]
  # it will help us to create data in there connected table very easy

  db.init_app(app)
  app.app_context().push()
  db.create_all()
  return app

app= create_app()





if __name__== "__main__":
  app.run()