from flask_restful import Api
from back.api.product import ProductApi
from back.api.order import OrderApi

api=Api()
api.add_resource(ProductApi, "/product", "/product/<int:id>",  methods=['GET', 'POST', 'PUT', 'DELETE'])
api.add_resource(OrderApi, "/order",  methods=['POST'])