"""
This code was written for the Nike warehouse.
The store manager can manage the warehouse and view the stock status of the products.
However, you can search for a product using the product code, identify and restock the product with the lowest stock,
find the product with the highest stock, and access the total values of all products separately,
and display all products with all their features.

"""

# 'tabulate' module added to get a better view.
from tabulate import tabulate


# Shoe class is defined. The Shoe class has 4 attribute which are 'country', 'code', 'product', 'cost' and 'quantity'.
# The Shoe class also has 3 module which are 'get_cost', get_quantity' and '__str__'.
# 'get close' module returns the cost of the shoe.
# 'get quantity' module returns the quantity of the shoe.
# '__str__' module returns the shoe's attributes as a string.
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return f"\nThe cost of the shoe: {self.cost}\n"

    def get_quantity(self):
        return f"\nThe quantity of the shoe: {self.quantity}\n"

    def __str__(self):
        return f"Country: {self.country}\nCode: {self.code}\n" \
               f"Product: {self.product}\nCost: {self.cost}\n" \
               f"Quantity: {self.quantity}\n"


# The list will be used to store a list of shoes objects.
shoe_list = []


# This  function opens the file inventory.txt and read the data from this file.
# Then creates a shoe object with this data and adds this object to the shoes list.
# In this code, try-except block is used to handle error.
def read_shoes_data():

    try:
        count = 0
        lines = 0
        with open("inventory.txt", "r") as file:

            for line in file:
                lines += 1

            file.seek(0)
            for line in file:
                if count == 0:
                    count += 1
                else:
                    line = line.strip("\n").split(",")
                    shoe = Shoe(line[0], line[1], line[2], line[3], line[4])
                    shoe_list.append(shoe)
                    count += 1

    except:
        print("Error.\n")


# This  function allows a user to capture data about a shoe and use this data to create a shoe object.
# Then function adds this object to the shoe list and writes in the file.
def capture_shoes():

    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = input("Enter the cost: ")
    quantity = input("Enter the quantity: ")

    shoe_list.append(Shoe(country, code, product, cost, quantity))

    with open("inventory.txt","a") as file:
        file.write(f"\n{country},{code},{product},{cost},{quantity}")

    print("\nThe product is captured.\n")


# This  function adds the shoes list to all_data list. Then it iterates over the all_data list
# And it prints the details of the shoes returned from the __str__ function with tabulate module.
def view_all():

    all_data = [["Country", "Code", "Product", "Cost", "Quantity"], []]

    for shoe in shoe_list:
        shoes = list()
        shoes.append(shoe.country)
        shoes.append(shoe.code)
        shoes.append(shoe.product)
        shoes.append(shoe.cost)
        shoes.append(shoe.quantity)
        all_data.append(shoes)

    print(tabulate(all_data))


# This  function finds the shoe object with the lowest quantity which needs to be re-stocked.
# Then asks the user if they want to add this quantity of shoes and then update it in the file and the shoe_list.
def re_stock():

    shoe_quantity = []

    for shoe in shoe_list:
        shoe_quantity.append(int(shoe.quantity))

    low = sorted(shoe_quantity)[0]

    for shoe in shoe_list:
        if int(shoe.quantity) == low:
            print(f"\n{shoe.product} is very low.\n")

            while True:
                want = input("Do you want to increase the amount of the product(Y/N): ")

                if want == "Y":

                    file = open("inventory.txt", "r+")
                    contents = file.readlines()
                    count = 0

                    for line in contents:
                        strip_line = line.strip("\n")
                        split_data = strip_line.split(",")
                        count += 1

                        if split_data[1] == shoe.code:
                            split_data[-1] = int(split_data[-1])
                            split_data[-1] += 1
                            split_data[-1] = str(split_data[-1])

                            join_data = ",".join(split_data)
                            contents[count-1] = join_data + "\n"
                            break

                    file.seek(0)
                    for line in contents:
                        file.write(line)
                    print("\nAdded.\n")

                    file.close()

                    shoe_list.clear()
                    read_shoes_data()
                    break

                elif want == "N":
                    print("\nNo product added!\n")
                    break

                else:
                    print("\nInvalid option!\n")
                    break


# This code searches for a shoe from the list using the shoe code and prints this object if it is found.
def search_shoe():
    search = input("Enter the shoe's code which you want to search: ")

    shoe_codes = []
    for shoe in shoe_list:
        shoe_codes.append(shoe.code)
        if shoe.code == search:
            print(f"\n{shoe}")

    if search not in shoe_codes:
        print("\nProduct not found.\n")


# This function calculates the total value for each item.
def value_per_item():

    for shoe in shoe_list:
        value = int(shoe.cost) * int(shoe.quantity)
        print(f"All {shoe.product}'s value is £{value}.\n")


# This function determines the product with the highest quantity and prints the shoe as being for sale.
def highest_qty():
    quantity_list = []

    for shoe in shoe_list:
        quantity_list.append(int(shoe.quantity))

    high = quantity_list[-1]

    for shoe in shoe_list:
        if int(shoe.quantity) == high:
            print(f"\n{shoe.product} is on sale.\n")


# The menu inside the while loop executes each function and modules above.
# In while loop, 'read_shoes_data' function is executed only 1 time and shoe_list is filled.
# Then user can choose an option from the menu.
count = 0

while True:

    if count == 0:
        read_shoes_data()
        count += 1

    else:
        option = input("What do you want to do: \n"
                       "1-Get Cost\n"
                       "2-Get Quantity\n"
                       "3-Capture a Product\n"
                       "4-Search a Product\n"
                       "5-View All Products\n"
                       "6-Restock\n"
                       "7-Value of All Product\n"
                       "8-Find Highest Quantity\n"
                       "9-Quit: ")

        if option == "9":
            print("\nBye!")
            break

        elif option == "1":
            product_name = input("Enter the product name which you want to show its cost: ")

            for shoe in shoe_list:
                if shoe.product == product_name:
                    print(shoe.get_cost())

        elif option == "2":
            product_name = input("Enter the product name which you want to show its quantity: ")

            for shoe in shoe_list:
                if shoe.product == product_name:
                    print(shoe.get_quantity())

        elif option == "3":
            capture_shoes()

        elif option == "4":
            search_shoe()

        elif option == "5":
            view_all()

        elif option == "6":
            re_stock()

        elif option == "7":
            value_per_item()

        elif option == "8":
            highest_qty()

        else:
            print("\nInvalid option!")
