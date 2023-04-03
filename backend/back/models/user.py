from back.models.base import BaseModel
from back.extensions import db



class User(BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    address=db.Column(db.String(80), nullable=False)
    orders = db.relationship('Order', backref='user', lazy=True)
    


