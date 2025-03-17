class Item:
    """Class representing an item with ID, name, description, and price."""

    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id} | Name: {self.name} | Description: {self.description} | Price: ${self.price:.2f}"


class ItemManager:
    """Manages CRUD operations for items."""

    def __init__(self):
        self.items = {}

    def create_item(self):
        """Creates a new item with validation."""
        try:
            item_id = input("Enter Item ID: ").strip()
            if item_id in self.items:
                raise ValueError("Error: Item ID already exists.")

            name = input("Enter Item Name: ").strip()
            if not name:
                raise ValueError("Error: Name cannot be empty.")

            description = input("Enter Item Description: ").strip()
            if not description:
                raise ValueError("Error: Description cannot be empty.")

            price = float(input("Enter Item Price: "))
            if price <= 0:
                raise ValueError("Error: Price must be greater than zero.")

            self.items[item_id] = Item(item_id, name, description, price)
            print("Item added successfully.")

        except ValueError as e:
            print(e)
        except Exception:
            print("Error: Invalid input. Please enter valid details.")

    def read_items(self):
        """Displays all items."""
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)

    def update_item(self):
        """Updates an existing item's details."""
        try:
            item_id = input("Enter Item ID to update: ").strip()
            if item_id not in self.items:
                raise ValueError("Error: Item ID not found.")

            name = input("Enter New Name (leave blank to keep current): ").strip()
            description = input("Enter New Description (leave blank to keep current): ").strip()
            price_input = input("Enter New Price (leave blank to keep current): ").strip()

            if name:
                self.items[item_id].name = name
            if description:
                self.items[item_id].description = description
            if price_input:
                price = float(price_input)
                if price <= 0:
                    raise ValueError("Error: Price must be greater than zero.")
                self.items[item_id].price = price

            print("Item updated successfully.")

        except ValueError as e:
            print(e)
        except Exception:
            print("Error: Invalid input. Please enter valid details.")

    def delete_item(self):
        """Deletes an item by ID."""
        try:
            item_id = input("Enter Item ID to delete: ").strip()
            if item_id not in self.items:
                raise ValueError("Error: Item ID not found.")

            del self.items[item_id]
            print("Item deleted successfully.")

        except ValueError as e:
            print(e)
        except Exception:
            print("Error: Invalid input. Please enter a valid ID.")

    def menu(self):
        """Displays the menu and handles user choices."""
        while True:
            print("\nItem Management System")
            print("[1] Create Item")
            print("[2] Read Items")
            print("[3] Update Item")
            print("[4] Delete Item")
            print("[5] Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.create_item()
            elif choice == "2":
                self.read_items()
            elif choice == "3":
                self.update_item()
            elif choice == "4":
                self.delete_item()
            elif choice == "5":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    manager = ItemManager()
    manager.menu()
