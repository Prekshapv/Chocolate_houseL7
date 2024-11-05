import models

def main():
    print("Welcome to the Chocolate House Management App")
    print("1. View Seasonal Flavors")
    print("2. Add New Seasonal Flavor")
    print("3. Exit")

    choice = input("Choose an option: ")
    if choice == '1':
        flavors = models.get_all_flavors()
        print("Seasonal Flavors:", flavors)
    elif choice == '2':
        name = input("Enter flavor name: ")
        availability = input("Enter availability: ")
        models.add_seasonal_flavor(name, availability)
        print("Flavor added!")
    elif choice == '3':
        print("Exiting...")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
