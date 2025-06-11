# Online Shopping Cart 

# - A shopping cart allows users to add products, remove products, view the cart, and calculate the total price. 
# - Products have attributes like name, price, and quantity. 
# - The program should provide a menu for users to select actions (e.g., Add Product, Remove Product, View Cart, Checkout). 
# - Use classes for Product and ShoppingCart. 

class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} x {self.quantity} = ${self.total_price():.2f}"


class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_product(self, name, price, quantity):
        key = name.lower()
        if name in self.cart:
            self.cart[name].quantity += quantity
            print(f"Added {quantity} more of {name} to the cart.")
        else:
            self.cart[name] = Product(name, price, quantity)
            print(f"Product {name} added to the cart.")

    def remove_product(self, name):
        if name in self.cart:
            del self.cart[name]
            print(f"Product {name} removed from the cart.")
        else:
            print("Product not found in cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("\nShopping Cart:")
            for product in self.cart.values():
                print(product)
            print(f"\nTotal: ${self.calculate_total():.2f}")

    def calculate_total(self):
        return sum(product.total_price() for product in self.cart.values())

    def checkout(self):
        if not self.cart:
            print("Your cart is empty. Nothing to checkout.")
        else:
            total = self.calculate_total()
            print("\nFinal Cart:")
            self.view_cart()
            print(f"Total amount due: ${total:.2f}")
            print("Thank you for shopping!")
            self.cart.clear()


def main():
    cart = ShoppingCart()

    while True:
        print("\nShopping Cart Menu:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter product name: ")
            try:
                price = float(input("Enter product price: "))
                quantity = int(input("Enter quantity: "))
                cart.add_product(name, price, quantity)
            except ValueError:
                print("Invalid input. Price must be a number, and quantity must be an integer.")
        elif choice == '2':
            name = input("Enter product name to remove: ")
            cart.remove_product(name)
        elif choice == '3':
            cart.view_cart()
        elif choice == '4':
            cart.checkout()
        elif choice == '5':
            print("Exiting Shopping Cart. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
