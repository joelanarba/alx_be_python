def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # ✅ Implement shopping_list as a list

    while True:
        display_menu()  # ✅ Call display_menu
        try:
            choice = int(input("Enter your choice: "))  # ✅ Input as integer
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"{item} added to shopping list.")
        elif choice == 2:
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from shopping list.")
            else:
                print(f"{item} not found in shopping list.")
        elif choice == 3:
            print("Current Shopping List:")
            for i in shopping_list:
                print(f"- {i}")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
