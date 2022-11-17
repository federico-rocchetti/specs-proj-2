import csv
from abc import ABC, abstractmethod
from pprint import pprint


# Classes for creating Cupcake Class for earlier parts of the Unit.
# Parent Class Cupcake.

class Cupcake(ABC):
    size = "regular"

    def __init__(self, name, cake, filling, frosting, price):
        self.name = name
        self.cake_flavor = cake
        self.filling = filling
        self.frosting_flavor = frosting
        self.sprinkles = []
        self.price = price
    
    def add_sprinkles(self, *args):
        for arg in args:
            self.sprinkles.append(arg)

    @abstractmethod 
    def calculate_price(self, quantity):
        return quantity * self.price


# Mini Cupcake Class

class Mini(Cupcake):
    size = "Mini"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price

mini_cupcake = Mini("Plain", 1.99, "Vanilla", "Vanilla")
mini_cupcake2 = Mini("Banana", 2.49, "Banana", "Banana")
mini_cupcake3 = Mini("Peanuts", 2.49, "Peanut Butter", "Peanut Butter Cream")

cupcake_list = [
    mini_cupcake,
    mini_cupcake2,
    mini_cupcake3
]

def write_new_csv(file, cupcakes):
    with open(file, 'w', newline='\n') as csvfile:
        fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'sprinkles', 'filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({'size': cupcake.size, 'name': cupcake.name, 'price': cupcake.price, 'flavor': cupcake.flavor, 'frosting': cupcake.frosting, 'sprinkles': cupcake.sprinkles, 'filling': cupcake.filling})
            else:
                writer.writerow({'size': cupcake.size, 'name': cupcake.name, 'price': cupcake.price, 'flavor': cupcake.flavor, 'frosting': cupcake.frosting, 'sprinkles': cupcake.sprinkles})


# Functions for final app functionality.

def read_csv(file):
    with open("sample.csv") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

# Get list with dictionaries for each cupcake in the csv file to render onto html.
def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

# Search for a particular cupcake by name in the csv.
def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

# Add cupcake to order.csv
def add_cupcake(file, cupcake):
    with open(file, 'a', newline='\n') as csvfile:
        fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'sprinkles', 'filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)
        
