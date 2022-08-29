from Magazyn import ITEMS, Product
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import DataRequired


def add_new_cargo(name,quantity,unit,unit_price):
    new_cargo = Product(name,quantity,unit,unit_price)
    return new_cargo

class AddCargoForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    quantity = IntegerField('quantity', validators=[DataRequired()])
    unit = StringField('unit', validators=[DataRequired()])
    unit_price = DecimalField('unit_price', validators=[DataRequired()])



class ProductSaleForm(FlaskForm):
    quantity_sell = IntegerField("quantity_sell", validators=[DataRequired()])



