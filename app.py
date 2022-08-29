from flask import Flask, redirect, render_template, request, make_response, jsonify, url_for, Response
from Magazyn import ITEMS, Product
from forms import add_new_cargo, AddCargoForm, ProductSaleForm
import json
import pandas as pd
import csv




app = Flask(__name__)

app.config["SECRET_KEY"] = "passsssword"


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)


@app.route("/cargo", methods = ["GET","POST"])
def current_state():
    form = AddCargoForm()
    list_of_products = ITEMS
    if request.method == "POST":
            new_cargo = Product(form.name.data,form.quantity.data,form.unit.data,form.unit_price.data)
    #strona startowa pokazująca obecny stan magazynowy oraz obecne saldo
    return render_template("products_list.html", list_of_products = list_of_products, form=form )




@app.route("/sell/<cargo_name>", methods = ["GET", "POST"])
def sell_cargo(cargo_name):
    form = ProductSaleForm()
    list_of_products = ITEMS
    if cargo_name not in list_of_products.keys():
        return redirect(url_for('current_state'))
    if request.method == "POST":
        amount_of_sell = form.quantity_sell.data
        if amount_of_sell is None:
            amount_of_sell = 0
        list_of_products[cargo_name].quantity = list_of_products[cargo_name].quantity - amount_of_sell
        return render_template("sale_product.html", cargo = cargo_name,list_of_products = list_of_products, form=form)
    return render_template("sale_product.html", cargo = cargo_name,list_of_products = list_of_products, form=form)


@app.route("/export_to_csv")
def export_to_csv():
    stock_status = [(ITEMS[item].__dict__)for item in ITEMS]
    keys = stock_status[0].keys()
    with open('magazyn.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(stock_status)
    return
