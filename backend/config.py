import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
  DEBUG= False
  # we don't interest to know baseconfig debgs
  SQL_ALCHEMY_TRACK_MODIFICATIONS= False 
  # SECURITY_UNAUTHORIZED_VIEW= None

class LocalDevlopmentConfig(BaseConfig):
  SQLALCHEMY_DATABASE_URI= "sqlite:///database.sqlite3"
  DEBUG=True 
  SECRET_KEY= os.environ.get("SECRET_KEY")
  SECURITY_PASSWORD_SALT= os.environ.get("SECURITY_PASSWORD_SALT")

  # SECURITY_PASSWORD_HASH= 'bcrypt'
  # SECURITY_KEY_AUTHORIZATION_HEADER = "Authentication-Token"
  # SECURITY_TOKEN_MAX_AGE= 3600
  # WTF_CSRF_ENABLED= False

class ProductionConfig(BaseConfig):
  DEBUG= False




