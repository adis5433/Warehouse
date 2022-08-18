import json
import copy
from subprocess import call
from unicodedata import name
import pandas as pd


ITEMS={}

class Product:
    next_item_id = 1
    def __init__(self, name, quantity, unit, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.unit_price = unit_price
        self.item_id = Product.next_item_id
        Product.next_item_id +=1
        ITEMS[self.name]=(self)
    
    
    def sell_cargo(self, sell_quantity):
        quantity_after_sell = self.quantity - sell_quantity
        self.quantity = quantity_after_sell
        income_from_cargo_sale = sell_quantity * self.unit_price
        return f"new quantity of product = {self.quantity} and income from sale ={income_from_cargo_sale}"

first_item=Product("milk" ,12000, "l", 3)
second_item=Product("flavour" ,11000, "kg", 2)
third_item=Product("sugar" ,30000, "kg", 4)
fourth_item=Product("salt" ,25000, "kg", 3)
fifth_item=Product("pepper" ,70000, "kg", 3)




dict_ITEMS=[(ITEMS[item].__dict__)for item in ITEMS]


print(type(dict_ITEMS[0]))








cargo = [{"Name" : "flavour", "Quantity" : 11000, "Unit" : "kg", "Price per unit": 2},
         {"Name" : "sugar", "Quantity" : 30000, "Unit" : "kg", "Price per unit": 4},
         {"Name" : "salt", "Quantity" : 25000, "Unit" : "kg", "Price per unit": 3},
         {"Name" : "pepper", "Quantity" : 70000, "Unit" : "kg", "Price per unit": 2}]
sold_cargo=[]





def round_to_two(num_to_round):
    return round(num_to_round,2)

def get_cost(list_of_cargo):
    total_value=0
    supply_value = [int(i["Quantity"])*int(i["Price per unit"]) for i in list_of_cargo]
    total_value = sum(supply_value)
    return total_value

def get_income():
    total_income = get_cost(sold_cargo)
    return total_income


def show_revenue():
    revenue = get_income() - get_cost(cargo)
    return revenue


def get_cargo(list = cargo):
    header = '{:<10}'.format("Name")+'{:^5}'.format("Quantity")+'{:^12}'.format("Unit")+'{:^15}'.format("Price per unit")
    print(header)
    print('{:=^44}'.format('') )
    for item in list:
        print('{:<10}'.format(item["Name"]),'{:^6}'.format(item["Quantity"]),'{:^12}'.format(item["Unit"]),'{:^15}'.format(item["Price per unit"]))


def add_cargo(item:str ,quantity: int,unit: str,value: int,list):
    add_stuff={}
    add_stuff.setdefault("Name",item)
    add_stuff.setdefault("Quantity",quantity)
    add_stuff.setdefault("Price per unit",value)
    add_stuff.setdefault("Unit", unit)
    list.append(add_stuff)
    return add_stuff

#funkcja update_sold_cargo przekazuje ilość sprzedanch do listy sold_cardo towarów żeby później obliczyć przychód
def update_sold_cargo(cargo_to_sell,sell_quantity):
    value_to_update = copy.deepcopy(cargo_to_sell)
    value_to_update["Quantity"] = sell_quantity
    sold_cargo.append(value_to_update)

def get_elem(name_of_cargo,list):
    for item in list:
        if item['Name'] == name_of_cargo:
            return item


def sell_cargo(stuff_to_sell, sell_quantity):
    cargo_to_sell = get_elem(stuff_to_sell,cargo)
    unit_of_cargo_to_sell = cargo_to_sell["Unit"]
    id_of_sold_cargo = cargo.index(cargo_to_sell)
    update_sold_cargo(cargo_to_sell,sell_quantity)
    cargo_to_sell["Quantity"] = int(cargo_to_sell["Quantity"])-int(sell_quantity)
    cargo[id_of_sold_cargo] = cargo_to_sell
    left_quantity = cargo[id_of_sold_cargo]["Quantity"]
    return f"afret sell {sell_quantity} {unit_of_cargo_to_sell} of {stuff_to_sell} in storage left {left_quantity} kg"



def export_items_to_csv():
    with open('magazyn.csv', 'w', newline='') as csvfile:
        fieldnames = list(cargo[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cargo)
        print("...succesfully saved data")

def load_items_from_csv():
    list.clear(cargo)
    with open('magazyn.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cargo.append(row)
    get_cargo(cargo)
    print("succesfilly data loaded")
    return cargo



