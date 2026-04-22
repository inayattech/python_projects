class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Name:{self.name} Price:{self.price}")

class CartItem:
    def __init__(self,product,quantity):
        self.product = product
        self.quantity = quantity

    # def get_total_price(self):
    #     return self.price * self.quantity    

class ShoppingCart:
    def __init__(self):
        self.items = []    
    
    def add_to_cart(self,product,quantity):
        if quantity <= 0:
            print("Invalid Quantity")
            return
        for item in self.items:
            if item.product.name == product.name:
                item.quantity += quantity
                print("Quantity Updated")
                return
        new_item = CartItem(product,quantity)
        self.items.append(new_item)  
        print("Item Added")

    def remove_item(self,product_name):
        for item in self.items:
            if item.product.name == product_name:
                self.items.remove(item)
                print("Removed")
                return
        print("Not Found")              

    def show_cart(self):
        for item in self.items:
            print(f"Product Name:{item.product.name} Price:{item.product.price} Quantity:{item.quantity}")

    def total_bill(self):
        total = 0
        for item in self.items:
            total += item.product.price * item.quantity
        print("Total:",total)    

product1 = Product("Headphone",1500)
product2 = Product("handfree",1000)

shop = ShoppingCart()
shop.add_to_cart(product1,1)
shop.show_cart()