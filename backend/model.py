from extensions import db 
from datetime import datetime, timezone
from flask_security.core import RoleMixin, UserMixin


class BaseModel(db.Model):
  # base model should not be a table bz we are not using it as table ;; so for that we have __abstract__
  __abstract__=True
  id= db.Column(db.Integer, primary_key=True)
  created_at= db.Column(db.DateTime(timezone=True), default= lambda:datetime.now(timezone.utc)) ## lambda fn we update time for each creation other wise it will compute once and use it every where ;; so when ever a data related to this table come this fn will run and set current time
  updated_at= db.Column(db.DateTime(timezone=True), default= lambda:datetime.now(timezone.utc), onupdate= lambda:datetime.now(timezone.utc))
# in DateTime why timezone bz flask sql alchemy has to recogize that this DataTime is time zone aware

class User(BaseModel, UserMixin):
  __tablename__= "users"
  username= db.Column(db.String(20), unique=True, nullable=False)
  email= db.Column(db.String, unique=True)
  password= db.Column(db.String, nullable=False, unique=True)
  fs_uniquifier= db.Column(db.String, unique= True, nullable= False) # this is auto added by flask security
  active= db.Column(db.Boolean, default= True) # if active=False, then the user will not be able to login

  roles= db.relationship('Role', backref= 'bearers', secondary='user_roles') # type: ignore
  requests= db.relationship("Request", back_populates='user', cascade="all, delete-orphan")
  sales= db.relationship('Sale', back_populates='user', cascade='all, delete-orphan')

class Role(BaseModel, RoleMixin):
  # when ever we use flask security ;; we use RoleMixin so flask security will know which is role mode and which is user model
  # and internally it is used that in order to create all that authentication, autherization
  name= db.Column(db.String, unique=True, nullable= False) ## this will for identify admin, manager, customer
  description= db.Column(db.String, nullable=False)


class UserRoles(BaseModel): 
  # it a many-to-many relationship so this table is saying which user has which roles # in this setup user can have multiple roles
  user_id= db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'))
  role_id= db.Column(db.Integer, db.ForeignKey("role.id", ondelete='CASCADE'))


class Manager(BaseModel):
  salary= db.Column(db.Integer)
  address= db.Column(db.String)
  department= db.Column(db.String)

  user_id= db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))

class Customer(BaseModel):
  loyalty_points= db.Column(db.Integer)

  user_id= db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))

class Request(BaseModel):
  """manager request to modify / update things and then it will be shown to admin"""
  data= db.Column(db.JSON())
  status= db.Column(db.Enum('Approved', 'Created', 'Rejected'))
  Type = db.Column(db.String)
  user_id= db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE' ), nullable=False)

  user= db.relationship('User', back_populates="requests")

class Section(BaseModel):
  __tablename__='section'
  name = db.Column(db.String(20), nullable= False)
  
  products= db.relationship("Product", back_populates='section', cascade= 'all, delete-orphan')

# why status_change_data should be in json format -> bz if a manager change section it will not be reflected, it will first go to the admin, and if admin approve this
# change then only those changes will be accepted -> status_chnage_data:JSON("status", "user_id", 'change':modify/del, "Type":"change name")
# now what we can do 1. put this Json is section that will capture the request, 2. A new request model
# so we will work on 2, making an another request model so through that we will direcly send those changes to admin


class Product(BaseModel):
  __tablename__="products"
  name = db.Column(db.String, nullable=False)
  price = db.Column(db.Numeric(10, 2), nullable=False) ## we don't use float instead use numeric bz it is more refine things;; in float we can't deside till how many decimal point value we want ; but in numeric we can
  stock = db.Column(db.Numeric(10,2))
  expiry = db.Column(db.DateTime(timezone=True))
  unit_of_sale = db.Column(db.Enum('Kg','Liter','Unit'))  # means -> kg, Liter, item(biskit) ;; to enforce this we can use "db.Enum" (Literal things in typing)
  mfd = db.Column(db.DateTime(timezone=True))

  section_id = db.Column(db.Integer,db.ForeignKey('section.id', ondelete='CASCADE'), nullable=False)

  section= db.relationship('Section', back_populates="products")
  saleItems= db.relationship('SaleItem', back_populates='product', cascade='all, delete-orphan')

class Sale(BaseModel):
  total_amount= db.Column(db.Numeric(10,2), nullable=False)
  customer_id= db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))

  user= db.relationship('User', back_populates='sales')
  saleItems= db.relationship('SaleItem', back_populates='sale', cascade='all, delete-orphan')

class SaleItem(BaseModel):
  product_id = db.Column(db.Integer, db.ForeignKey('products.id',ondelete='CASCADE'),nullable=False)
  quantity = db.Column(db.Numeric(10,2))
  price_at_sale = db.Column(db.Numeric(10, 2), nullable=False)
  sale_id= db.Column(db.Integer,db.ForeignKey('sale.id', ondelete='CASCADE'), nullable=False)

  sale= db.relationship('Sale', back_populates='saleItems')
  product= db.relationship('Product', back_populates='saleItems')