from flask.cli import with_appcontext
import click
from back.extensions import db
from back.models.product import Product
from back.models.user import User
import csv
import os
from flask import current_app

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Finished Creating Database")


@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Creating items")

    fields=['name', 'description', 'price']

    # dummy_data=[{"name": "Latte", "description":"Coffee drink made with espresso and steamed milk", "price":"6.30"},
    #             {"name": "Mocha", "description":"Coffee drink made with espresso, chocolate sauce and steamed milk", "price":"7.25"},
    #             {"name": "Americano", "description":"Coffee prepared by adding hot water to espresso", "price":"4.25"}, 
    #             {"name": "Espresso", "description":"Espresso - a strong, perfect coffee flavor", "price":"4.00"}, 
    #             {"name": "Cappuccino", "description":"Coffee prepared with espresso, hot milk and steamed-milk foam", "price":"6.00"}, 
    #             {"name": "Specialty Drinks", "description":"Mocha, White Chocolate Mocha, Mayan Mocha, Crème Brule, Turtle Sundae, Cinnamon Spice, Chocolate Covered Cherry, Grasshopper, Nutty Irish, Raspberry Clouds", "price":"9.75"}]
    
    
    # with open (os.path.join(current_app.config['BASE_DIR'], 'csv', 'coffee.csv'), mode='w') as coffee_csv:
    #     writer=csv.DictWriter(coffee_csv, fieldnames=fields)
    #     writer.writeheader()
    #     writer.writerows(dummy_data)
    path=os.path.join(current_app.config['BASE_DIR'], 'csv', 'coffee.csv')
    with open(path, "r", encoding='ISO-8859-1') as coffee_csv:
        csv_reader= csv.DictReader(coffee_csv)
        for row in csv_reader:
            new_item = Product(name=row['name'], description=row['description'], price=row['price'])
            new_item.create()


    click.echo("Creating users")
    testuser = User(email="admin@mail.com", name="testuser", phone="599546546", address='askjdahsjd')
    testuser.create()

