class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def display_inventory(self):
        print("Inventory:")
        for item in self.items:
            print("- {} ({}): ${}".format(item.name, item.quantity, item.price))

    def calculate_total_value(self):
        total_value = 0
        for item in self.items:
            total_value += item.price * item.quantity
        return total_value

# Crear algunos objetos de ejemplo
item1 = Item("Laptop", 2, 1000)
item2 = Item("Smartphone", 5, 500)
item3 = Item("Tablet", 3, 800)

# Crear un objeto de inventario y agregar los elementos
inventory = Inventory()
inventory.add_item(item1)
inventory.add_item(item2)
inventory.add_item(item3)

# Mostrar el inventario y el valor total
inventory.display_inventory()
print("Total value: ${}".format(inventory.calculate_total_value()))

def display_menu():
    print("\nMenu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display inventory")
    print("4. Calculate total value")
    print("5. Quit")


while True:
    display_menu()
    choice = input("\nEnter an option: ")

    if choice == "1":
        name = input("Enter item name: ")
        quantity = int(input("Enter item quantity: "))
        price = float(input("Enter item price: "))
        item = Item(name, quantity, price)
        inventory.add_item(item)
        print("{} added to inventory.".format(name))

    elif choice == "2":
        name = input("Enter item name to remove: ")
        for item in inventory.items:
            if item.name == name:
                inventory.remove_item(item)
                print("{} removed from inventory.".format(name))
                break
        else:
            print("{} not found in inventory.".format(name))

    elif choice == "3":
        inventory.display_inventory()

    elif choice == "4":
        total_value = inventory.calculate_total_value()
        print("Total value: ${}".format(total_value))

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
