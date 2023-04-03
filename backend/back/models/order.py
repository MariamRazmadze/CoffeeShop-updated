from back.models.base import BaseModel
from back.extensions import db
import datetime
from back.models.product import Product

class Order(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    total=db.Column(db.Float)
    items = db.relationship('OrderItem', backref='order', lazy=True)

    def __init__(self, user_id):
        self.user_id = user_id

    def set_total(self):
        total = 0
        for item in self.items:
            product = Product.query.get(item.product_id)
            total += product.price * item.amount
        self.total = total