from library.extension import db
from flask_jwt_extended import get_jwt_identity
class Users(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(50),nullable = False)
    username = db.Column(db.String(20),nullable = False)
    password = db.Column(db.String(20),nullable = False) 

    def __init__(self, email,username, password):
        self.email = email    
        self.username = username
        self.password = password

class Admin(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(50),nullable = False)
    adminname = db.Column(db.String(20),nullable = False)
    password = db.Column(db.String(20),nullable = False) 

    def __init__(self, email,adminname, password):
        self.email = email    
        self.adminname = adminname
        self.password = password

class Total_price(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    price_value = db.Column(db.Integer,nullable = False)
    product_value = db.Column(db.Integer,nullable = False)
    men_price = db.Column(db.Integer,nullable = False)
    women_price = db.Column(db.Integer,nullable = False)
    men_product = db.Column(db.Integer,nullable = False)
    women_product = db.Column(db.Integer,nullable = False)
    label = db.Column(db.String(50),nullable = False)

    def __init__(self,price_value,product_value,men_price,women_price,men_product,women_product,label):
        self.price_value = price_value
        self.product_value =product_value
        self.men_price =men_price
        self.women_price =women_price
        self.men_product =men_product
        self.women_product =women_product
        self.label=label 

class Feedback_data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    phone_fb = db.Column(db.Integer,nullable = False)
    email_fb = db.Column(db.String(50),nullable = False)
    user_fb = db.Column(db.String(50),nullable = False)
    mess_fb = db.Column(db.String(500),nullable = False)

    def __init__(self,phone_fb,email_fb,user_fb,mess_fb):
        self.phone_fb =phone_fb
        self.email_fb =email_fb
        self.user_fb =user_fb
        self.mess_fb =mess_fb       

class Customer_data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    phone_ct= db.Column(db.Integer,nullable = False)
    email_ct= db.Column(db.String(50),nullable = False)
    user_ct= db.Column(db.String(50),nullable = False)
    mess_ct= db.Column(db.String(500),nullable = False)
    address_ct= db.Column(db.String(50),nullable = False)
    pass_ct = db.Column(db.String(20),nullable = False) 

    def __init__(self,phone_ct,email_ct,user_ct,mess_ct,address_ct,pass_ct):
        self.phone_ct=phone_ct
        self.email_ct=email_ct
        self.user_ct=user_ct
        self.mess_ct=mess_ct
        self.address_ct = address_ct
        self.pass_ct = pass_ct

class Image_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)
    image_name = db.Column(db.String(255), nullable=False)
    type_name = db.Column(db.String(255), nullable=False)
    size_value = db.Column(db.String(255), nullable=False)
    price_value = db.Column(db.Integer, nullable=False)

    def __init__(self, image_url, price_value, image_name, type_name, size_value):
        self.image_url = image_url
        self.price_value = price_value
        self.image_name = image_name
        self.type_name = type_name
        self.size_value = size_value
        


