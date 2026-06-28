from load_inventory import load_inventory
from save_inventory import save_inventory
from add_items import add_item
from distribute_aid import distribute_aid
from generate_report import generate_report
from search_item import search_item

filename = "aid_inventory.txt"
inventory = load_inventory(filename)

while True:
    print("\n===== Humanitarian Aid Tracker =====")
    print("1. Add Shipment")
    print("2. Distribute Aid")
    print("3. Inventory Report")
    print("4. Search Item")
    print("5. Save & Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_item(inventory)

    elif choice == "2":
        distribute_aid(inventory)

    elif choice == "3":
        generate_report(inventory)

    elif choice == "4":
        search_item(inventory)

    elif choice == "5":
        save_inventory(filename, inventory)
        print("Inventory saved successfully.")
        print("Goodbye!")
        break

    else:
        print("Invalid option.")