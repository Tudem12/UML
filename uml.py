# Class to represent Products
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"

# Class to represent a Customer
class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def browse_products(self, store):
        print(f"{self.name} is browsing the store...")
        store.show_products()

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"{product.name} added to cart.")

    def place_order(self):
        total = sum([product.price for product in self.cart])
        print(f"Order placed by {self.name} for ${total}.")
        self.cart.clear()

# Class to represent an Administrator
class Administrator:
    def __init__(self, name):
        self.name = name

    def manage_users(self, store, action, customer=None):
        if action == 'add' and customer:
            store.add_customer(customer)
            print(f"{self.name} added {customer.name} as a customer.")
        elif action == 'remove' and customer:
            store.remove_customer(customer)
            print(f"{self.name} removed {customer.name} from the system.")
        else:
            print(f"Invalid action or missing customer.")

# Class to represent the Online Store
class OnlineStore:
    def __init__(self):
        self.products = []
        self.customers = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        print("Available Products:")
        for product in self.products:
            print(product)

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer):
        if customer in self.customers:
            self.customers.remove(customer)

# Main Program to simulate the Use Case diagram actions

# Initialize Store and Products
store = OnlineStore()
store.add_product(Product("Laptop", 1000))
store.add_product(Product("Smartphone", 800))
store.add_product(Product("Headphones", 150))

# Create Customers and Admin
customer1 = Customer("Alice")
customer2 = Customer("Bob")
admin = Administrator("Charlie")

# Simulating use cases
customer1.browse_products(store)
customer1.add_to_cart(store.products[0])  # Adding Laptop to the cart
customer1.add_to_cart(store.products[1])  # Adding Smartphone to the cart
customer1.place_order()

# Admin managing users
admin.manage_users(store, 'add', customer2)  # Adding Bob to the store
admin.manage_users(store, 'remove', customer1)  # Removing Alice from the store
