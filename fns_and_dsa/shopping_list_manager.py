def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = int(input("Enter your choice: "))  # ✅ EXACTLY like this

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
            if not shopping_list:
                print("The shopping list is empty.")
            for item in shopping_list:
                print(f"- {item}")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
