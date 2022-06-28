import csv
import copy

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

def our_storage(command : str, cargo: list):
        match command.split():
            case ["warehouse" |"ware"|"commodity"|"stuff"]:
                print(get_cargo(cargo))
            case ["+"|"add" |"storage"]:
                name_of_cargo = input("what cargo we add...")
                unit = input("what is unit of measure...")
                quantity = int(input(f"how much of {unit} {name_of_cargo} we add..."))
                value_of_cargo = int(input(f"what value per {unit} for {name_of_cargo}..."))
                print(f"adding {quantity}{unit} of {name_of_cargo}")
                print(add_cargo(name_of_cargo, quantity, unit,value_of_cargo, cargo))
            case ["-"|"sell" |"extradition"|"release"]:
                stuff_to_sell = input("what you want tu sell: ")
                sell_quantity = int(input(f"How much of {stuff_to_sell} you want to sell: "))
                print(f"selling {sell_quantity} kg of {stuff_to_sell}")
                print(sell_cargo(stuff_to_sell,sell_quantity))
                get_cargo()
            case ["revenue" | "result" | "balance"]:
                print("Values are in PLN")
                print("Total income: ",round_to_two(get_income()))
                print("Cost: ", round_to_two(get_cost(cargo)))
                print("Revenue: ",round_to_two(show_revenue()))
            case ["save"]:
                export_items_to_csv()
            case ["load"]:
                load_items_from_csv()
            case ["exit" |"close"|"quit"]:
                print("We're closing app")
                exit()
            case [_]:
                print("Option not in menu. Please choose option from menu")





if __name__ == "__main__":
    load_items_from_csv()
    print("Welcome in our_storage app")
    while True:
        try:
            print("Menu:\n"
                    "warehouse/ware/commodity/stuff.....show  current cargo in warehouse\n"
                    "+/add/storage......................add new cargo\n"
                    "-/sell/extradition/release.........sell cargo\n"
                    "revenue/result/balance.............show current balance\n"
                    "save...............................save changes\n"
                    "load...............................load file with data\n"
                    "exit/close/quit....................exit program\n"
                    "What do you want to do?")
            command = input("$ ")
            our_storage(command,cargo)
        except ValueError:
            print("Incorrect value!")

