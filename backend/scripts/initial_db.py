# it like a scripts which will feed intial data;; run it once that it will feed certain kind of data 
# to test

## first want to create some users

from app import app
from model import db
from flask_security.utils import hash_password
from flask_security.datastore import SQLAlchemyUserDatastore

with app.app_context():
  db.drop_all() # will delete all data
  db.create_all() # and create fresh data base
  datastore:SQLAlchemyUserDatastore = app.datastore

  admin_role= datastore.find_or_create_role('admin', description="super user")
  manager_role= datastore.find_or_create_role('manager', description="handles and manges store")
  customer= datastore.find_or_create_role('customer', description="buy items from store")

  if not datastore.find_user(email="admin@study"): # let admin has a unique gmail so here we first checking that if that email doesn't have in datastore then create an admin  
    datastore.create_user(
      email="admin@study",
      username='Adi',
      password=hash_password('admin_01')
    )

  if not datastore.find_user(email="manager@study"):
    datastore.create_user(
      email= "manager@study",
      username= 'manager0',
      password= hash_password('manager_01')
      
    )
  if not datastore.find_user(email='customer@study'):
    datastore.create_user(
      email= 'customer@study',
      username= 'customer0',
      password=hash_password("customer01")
    )


  # if we will be written in plan text which is not good
  # so before that we have to hashed it;; so for that flask_security.utils gives us hasded password;; so we will use it to hased it

  try:
    db.session.commit()
  except:
    db.session.rollback()
    print("Error during creating")

  # after commit let try to add that mapping thing from user-> role

  admin01= datastore.find_user(email='admin@study')
  manager01= datastore.find_user(email='manager@study')
  customer01= datastore.find_user(email='customer@study')

  admin_role= datastore.find_role('admin')
  manager_role= datastore.find_role('manager')
  customer_role= datastore.find_role('customer')

  datastore.add_role_to_user(admin01, admin_role)
  datastore.add_role_to_user(manager01, manager_role)
  datastore.add_role_to_user(customer01, customer_role)

  try:
    db.session.commit()
    print('successfully assigned the roles to admin, manager, customer')
  except:
    db.session.rollback()
    print('Error during assigning the role')