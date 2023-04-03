from back.extensions import db
from back.models.base import BaseModel

class Product(BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text(500))
    price = db.Column(db.Float(precision=2))
    orders = db.relationship('OrderItem', backref='product', lazy=True)

 

    


