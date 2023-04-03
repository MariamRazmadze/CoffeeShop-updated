from flask_restful import Resource, reqparse
from back.models.product import Product


class ProductApi(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="name is required")
    parser.add_argument("description", type=str, required=True, help="description is required")
    parser.add_argument("price", type=float, required=True, help="price is required")
    

    def get(self):
        products=Product.query.all()
        product_json=[]
        for product in products:
            product_info={
                "id":product.id, 
                "name": product.name, 
                "description": product.description, 
                "price": product.price
            }
            product_json.append(product_info)
        return product_json, 200
        
 
    def post(self):
        parser=self.parser.parse_args()
        new_product=Product(name=parser['name'], description=parser['description'], price=parser['price'])
        new_product.create()
        return new_product.id, 200
    
    def put(self, id):
        parser=self.parser.parse_args()
        chosen_product=Product.query.get(id)
        if not chosen_product: return "Product not found", 404
        chosen_product.name=parser['name']
        chosen_product.description=parser['description']
        chosen_product.price=parser['price']
        chosen_product.save()
        return 'success', 200
    

    def delete(self, id):
        chosen_product=Product.query.get(id)
        if chosen_product:
            chosen_product.delete()
            return 'success', 200
        else:
            return 'product not found', 404



        

