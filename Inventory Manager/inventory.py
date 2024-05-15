# ============ Load Modules ===============

from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
    
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return(self.cost)
        
    def get_quantity(self):
        return(self.quantity)

    def __str__(self):
        return(f"\nProduct: {self.product}\nCode: {self.code}\nCost: {self.cost}\nQuantity: {self.quantity}\nCountry: {self.country}")

#=============Shoe list===========

shoe_list = []

#==========Functions outside the class==============

# Function to read data from external data file
def read_shoes_data():

    try:
        with open("inventory.txt","r",encoding="UTF-8") as loadfile:
            for line in loadfile:
                split_line = line.split(",")
                new_shoe = Shoe(split_line[0],split_line[1],split_line[2],split_line[3],split_line[4])
                shoe_list.append(new_shoe)
                new_shoe = []
        del shoe_list[0]

    except FileNotFoundError:
        print("No load file can be found")

# Function to add a new shoe
def capture_shoes():

    input_product = input("Enter Product Name: ")
    input_country = input("Enter Product Country: ")
    input_code = int(input("Enter Product Code: "))
    input_cost = float(input("Enter Product Cost: "))
    input_quantity = int(input("Enter Stock Quanity: "))

    new_shoe = Shoe(input_country,input_code,input_product,input_cost,input_quantity)
    shoe_list.append(new_shoe)

# Function to print all shoe data in a table
def view_all():
        table = [["Country","Code","Product","Cost","Quantity"]]
        for item in shoe_list:
            row = [item.country, item.code, item.product, item.cost, item.quantity]
            table.append(row)
        print(tabulate(table))

# Function returns the shoe with the lowest quantity and offers the opertunity to add stock
def re_stock():
        min_quantity = shoe_list[0].quantity
        for index, item in enumerate(shoe_list):
             if item.quantity < min_quantity:
                  min_quantity = item.quantity
                  min_index = index
        print(f"The lowest stock item is: \nProduct: {shoe_list[index].product}\nCode: {shoe_list[index].code}\nQuantity: {shoe_list[index].quantity}")
        user_input = input("Would you like to restock the item? Yes or No? ")
        try:
            if user_input.lower() == "yes":
                 new_quantity = int(input("What is the new quantity? "))
                 shoe_list[index].quantity = new_quantity
                  
            if user_input.lower() == "no":
                 pass
        except Exception:
            print("Not a valid selection")

# Function accepts a product code and prints the details of the matching product
def search_shoe(code):
     for index, item in enumerate(shoe_list):
          if item.code == code:
            print(item)
          else:
            print("No product found")

# Function to calculate and print table of product stock values
def value_per_item():
    value_table = [["Product","Total Value"]]
    for item in shoe_list:
        value = float(item.cost) * int(item.quantity)
        value_row = [item.product,value]
        value_table.append(value_row)
    print(tabulate(value_table))

# Function finds the item with the highest qaunitity and suggests putting it on sale
def highest_qty():
    max_quantity = shoe_list[0].quantity
    for index, item in enumerate(shoe_list):
            if item.quantity > max_quantity:
                max_quantity = item.quantity
                max_index = index
    print(f"Put {shoe_list[max_index].product} on sale.") 

# Programe
read_shoes_data()
menu_select = 0
restart = True
while restart == True:
    try:
        menu_select = int(input("""
-----------Menu----------
1. View all
2. Add product
3. Restock
4. Search
5. Stock Value
6. Product to discount
7. Quit 
"""))
        if menu_select == 1:
            view_all()

        elif menu_select == 2:
            capture_shoes()
    
        elif menu_select == 3:
            re_stock()

        elif menu_select == 4:
            search_value = input("Enter code of shoe to search for: ")
            search_shoe(search_value)

        elif menu_select == 5:
            value_per_item()

        elif menu_select == 6:
            highest_qty()

        elif menu_select == 7:
            restart = False

        else:
            print("Not a valid selection")

    except Exception:
        print("Not a valid selction")
