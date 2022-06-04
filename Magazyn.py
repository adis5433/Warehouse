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
    supply_value = [i["Quantity"]*i["Price per unit"] for i in list_of_cargo]
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

def sell_cargo(stuff_to_sell, sell_quantity, list_of_cargo = cargo,list_of_sold_items = sold_cargo):
    state_to_change = get_elem(stuff_to_sell,list_of_cargo)
    unit = state_to_change["Unit"]
    id_of_sold_cargo =list_of_cargo.index(state_to_change)
    new_value = copy.deepcopy(state_to_change)
    new_value["Quantity"]=sell_quantity
    list_of_sold_items.append(new_value)
    state_to_change["Quantity"] = state_to_change["Quantity"]-sell_quantity
    list_of_cargo[id_of_sold_cargo]=state_to_change
    left_quantity = list_of_cargo[id_of_sold_cargo]["Quantity"]
    return f"afret sell {sell_quantity} {unit} of {stuff_to_sell} in storage left {left_quantity} kg"

def get_elem(name_of_cargo,list):
    for item in list:
        if item['Name'] == name_of_cargo:
            return item



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
        case ["exit" |"close"|"quit"]:
            print("We're closing app")
            exit()




if __name__ == "__main__":
    while(True):
        print("Welcome in our_storage app, what you want to do")
        command = input("$ ")
        our_storage(command,cargo)