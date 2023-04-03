from flask_restful import Resource, reqparse
from back.models.user import User
from back.models.order import Order
from back.models.orderitem import OrderItem
from back.models.product import Product


class OrderApi(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument("user", type=dict,  required=True, help="user is required")
    parser.add_argument("orderedItems", type=dict,  action="append", required=True, help="orderedItems is required")
    
 
    def post(self):
        parser=self.parser.parse_args()
        user_data=parser['user']
        new_user=User(name=user_data['name'], phone=user_data['phone'], email=user_data['email'], address=user_data['address'])
        new_user.create()


        order = Order(user_id=new_user.id)
        order.create()
      
        for item in parser['orderedItems']:
            print(parser['orderedItems'])
            id_mapping=Product.query.filter_by(name=item['name']).first()
            product_id=id_mapping.id
            amount = item.get('amount')
            new_item = OrderItem(order_id=order.id, product_id=product_id, amount=amount)
            order.items.append(new_item)
            new_item.create()
        
        order.set_total()
        order.save()

        return {'id': order.id}






       